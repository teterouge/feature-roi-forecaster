#!/usr/bin/env python3
"""
roi_model.py — Three-scenario ROI model for feature investment decisions.

Runs conservative, base, and optimistic scenarios given structured inputs.
Outputs a formatted table with net ROI, payback period, and cost of delay.

Usage:
    python roi_model.py --interactive
    python roi_model.py --input inputs.json
    python roi_model.py --input inputs.json --format json

Input JSON format:
{
  "feature_name": "Guided Onboarding Checklist",
  "metric_type": "revenue",           // "revenue" | "cost_reduction"
  "affected_population": 2000,        // users/accounts in scope per month
  "baseline_metric": 0.35,            // current conversion/retention/etc rate
  "lift_conservative": 0.08,          // absolute lift (not relative) - conservative
  "lift_base": 0.12,                  // absolute lift - base
  "lift_optimistic": 0.18,            // absolute lift - optimistic
  "adoption_rate": 1.0,               // % of affected population who will use feature
  "revenue_per_unit": 66.67,          // revenue or cost saved per converted unit/month
  "engineering_cost": 40000,          // total fully-loaded build cost
  "time_to_impact_months": 1,         // months from launch until metric moves
  "model_window_months": 12           // months to model (default 12)
}
"""

import sys
import json
import argparse
from typing import Optional


# ---------------------------------------------------------------------------
# Core model
# ---------------------------------------------------------------------------

def run_scenario(
    affected_population: float,
    lift: float,
    adoption_rate: float,
    revenue_per_unit: float,
    engineering_cost: float,
    time_to_impact_months: int,
    model_window_months: int,
    metric_type: str = "revenue",
) -> dict:
    """Run a single scenario and return key metrics."""

    # Months with impact (after ramp)
    active_months = model_window_months - time_to_impact_months
    if active_months <= 0:
        active_months = 0

    # Monthly incremental value
    monthly_incremental_units = affected_population * adoption_rate * lift
    monthly_value = monthly_incremental_units * revenue_per_unit

    # Total value over model window
    total_value = monthly_value * active_months

    # Net ROI
    net_roi = total_value - engineering_cost

    # Payback period (months)
    if monthly_value > 0:
        payback_months = engineering_cost / monthly_value
    else:
        payback_months = float('inf')

    # Cost of delay per month
    cost_of_delay = monthly_value

    # ROI percentage
    if engineering_cost > 0:
        roi_pct = (net_roi / engineering_cost) * 100
    else:
        roi_pct = float('inf')

    return {
        "monthly_value": monthly_value,
        "total_value": total_value,
        "engineering_cost": engineering_cost,
        "net_roi": net_roi,
        "roi_pct": roi_pct,
        "payback_months": payback_months,
        "cost_of_delay_monthly": cost_of_delay,
        "active_months": active_months,
        "monthly_incremental_units": monthly_incremental_units,
    }


def format_currency(value: float) -> str:
    """Format a number as currency."""
    if value == float('inf'):
        return "∞"
    if abs(value) >= 1_000_000:
        return f"${value/1_000_000:.1f}M"
    if abs(value) >= 1_000:
        return f"${value/1_000:.0f}K"
    return f"${value:.0f}"


def format_months(value: float) -> str:
    """Format payback period."""
    if value == float('inf'):
        return "Never"
    if value > 120:
        return ">10 years"
    if value < 1:
        return "<1 month"
    return f"{value:.1f} months"


def format_pct(value: float) -> str:
    """Format ROI percentage."""
    if value == float('inf'):
        return "∞%"
    return f"{value:.0f}%"


# ---------------------------------------------------------------------------
# Output formatters
# ---------------------------------------------------------------------------

def format_text_output(feature_name: str, inputs: dict,
                       conservative: dict, base: dict, optimistic: dict) -> str:
    """Format human-readable three-scenario table."""
    lines = []
    lines.append(f"\nFEATURE ROI MODEL — {feature_name.upper()}")
    lines.append(f"Model window: {inputs.get('model_window_months', 12)} months")
    lines.append(f"Time to impact: {inputs.get('time_to_impact_months', 1)} month(s)")
    lines.append("=" * 65)

    # Inputs summary
    lines.append("\nINPUTS USED:")
    lines.append(f"  Affected population:    {inputs['affected_population']:,.0f} units/month")
    lines.append(f"  Adoption rate:          {inputs['adoption_rate']*100:.0f}%")
    lines.append(f"  Revenue/cost per unit:  {format_currency(inputs['revenue_per_unit'])}/month")
    lines.append(f"  Engineering cost:       {format_currency(inputs['engineering_cost'])}")
    lines.append(f"  Lift (conservative):    +{inputs['lift_conservative']*100:.1f}pp")
    lines.append(f"  Lift (base):            +{inputs['lift_base']*100:.1f}pp")
    lines.append(f"  Lift (optimistic):      +{inputs['lift_optimistic']*100:.1f}pp")

    # Results table
    lines.append(f"\n{'METRIC':<32} {'CONSERVATIVE':>10} {'BASE':>10} {'OPTIMISTIC':>10}")
    lines.append("-" * 65)

    rows = [
        ("Monthly incremental units",
         f"{conservative['monthly_incremental_units']:.0f}",
         f"{base['monthly_incremental_units']:.0f}",
         f"{optimistic['monthly_incremental_units']:.0f}"),
        ("Monthly value",
         format_currency(conservative['monthly_value']),
         format_currency(base['monthly_value']),
         format_currency(optimistic['monthly_value'])),
        (f"Total value ({inputs.get('model_window_months',12)}mo)",
         format_currency(conservative['total_value']),
         format_currency(base['total_value']),
         format_currency(optimistic['total_value'])),
        ("Engineering cost",
         format_currency(conservative['engineering_cost']),
         format_currency(base['engineering_cost']),
         format_currency(optimistic['engineering_cost'])),
        ("Net ROI",
         format_currency(conservative['net_roi']),
         format_currency(base['net_roi']),
         format_currency(optimistic['net_roi'])),
        ("ROI %",
         format_pct(conservative['roi_pct']),
         format_pct(base['roi_pct']),
         format_pct(optimistic['roi_pct'])),
        ("Payback period",
         format_months(conservative['payback_months']),
         format_months(base['payback_months']),
         format_months(optimistic['payback_months'])),
        ("Cost of delay / month",
         format_currency(conservative['cost_of_delay_monthly']),
         format_currency(base['cost_of_delay_monthly']),
         format_currency(optimistic['cost_of_delay_monthly'])),
    ]

    for label, c_val, b_val, o_val in rows:
        lines.append(f"{label:<32} {c_val:>10} {b_val:>10} {o_val:>10}")

    lines.append("=" * 65)

    # Quick verdict
    if base['net_roi'] > 0 and conservative['net_roi'] > 0:
        verdict = "✅ POSITIVE ROI across all scenarios"
    elif base['net_roi'] > 0 and conservative['net_roi'] <= 0:
        verdict = "⚠️  POSITIVE in base/optimistic, NEGATIVE in conservative"
    else:
        verdict = "❌ NEGATIVE ROI — base case does not justify investment"

    lines.append(f"\nQUICK VERDICT: {verdict}")

    if base['payback_months'] != float('inf'):
        lines.append(f"Base case payback: {format_months(base['payback_months'])}")

    lines.append(f"Cost of delay (base): {format_currency(base['cost_of_delay_monthly'])}/month")
    lines.append("")

    return '\n'.join(lines)


def format_json_output(feature_name: str, inputs: dict,
                       conservative: dict, base: dict, optimistic: dict) -> str:
    """Format as JSON for further processing."""
    return json.dumps({
        "feature_name": feature_name,
        "inputs": inputs,
        "scenarios": {
            "conservative": conservative,
            "base": base,
            "optimistic": optimistic,
        },
        "summary": {
            "base_net_roi": base['net_roi'],
            "base_payback_months": base['payback_months'] if base['payback_months'] != float('inf') else None,
            "cost_of_delay_monthly_base": base['cost_of_delay_monthly'],
            "positive_in_all_scenarios": conservative['net_roi'] > 0,
            "positive_in_base": base['net_roi'] > 0,
        }
    }, indent=2, default=lambda x: None if x == float('inf') else x)


# ---------------------------------------------------------------------------
# Interactive mode
# ---------------------------------------------------------------------------

def prompt_float(label: str, default: Optional[float] = None) -> float:
    """Prompt for a float value with optional default."""
    hint = f" [{default}]" if default is not None else ""
    while True:
        raw = input(f"  {label}{hint}: ").strip()
        if not raw and default is not None:
            return float(default)
        try:
            return float(raw)
        except ValueError:
            print(f"  Please enter a number.")


def interactive_mode() -> dict:
    """Collect inputs interactively."""
    print("\nFEATURE ROI FORECASTER — Interactive Input")
    print("=" * 50)
    print("Press Enter to accept defaults where shown.\n")

    inputs = {}
    inputs['feature_name'] = input("  Feature name: ").strip() or "Feature"

    print("\n  Metric type:")
    print("    1. Revenue (conversion, retention, expansion)")
    print("    2. Cost reduction (support deflection, automation)")
    choice = input("  Choice [1]: ").strip() or "1"
    inputs['metric_type'] = "revenue" if choice == "1" else "cost_reduction"

    print()
    inputs['affected_population'] = prompt_float("Affected population (users/accounts/month)")
    inputs['adoption_rate'] = prompt_float("Adoption rate (0.0–1.0, e.g. 0.8 = 80%)", 1.0)
    inputs['revenue_per_unit'] = prompt_float(
        "Revenue or cost saved per unit per month ($)" +
        ("\n    Tip: for annual ACV, divide by 12" if inputs['metric_type'] == 'revenue' else "")
    )
    inputs['lift_base'] = prompt_float("Expected lift — base case (e.g. 0.10 = 10pp improvement)")
    inputs['lift_conservative'] = prompt_float(
        "Expected lift — conservative (bottom quartile)",
        round(inputs['lift_base'] * 0.65, 4)
    )
    inputs['lift_optimistic'] = prompt_float(
        "Expected lift — optimistic (top quartile)",
        round(inputs['lift_base'] * 1.5, 4)
    )
    inputs['engineering_cost'] = prompt_float("Engineering cost — fully loaded ($)")
    inputs['time_to_impact_months'] = int(prompt_float("Time to impact (months from launch)", 1))
    inputs['model_window_months'] = int(prompt_float("Model window (months)", 12))

    return inputs


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description='Three-scenario ROI model for feature investment decisions.'
    )
    parser.add_argument('--input', help='Path to JSON inputs file')
    parser.add_argument('--interactive', action='store_true', help='Collect inputs interactively')
    parser.add_argument('--format', choices=['text', 'json'], default='text', help='Output format')

    args = parser.parse_args()

    if args.interactive:
        inputs = interactive_mode()
    elif args.input:
        with open(args.input, 'r') as f:
            inputs = json.load(f)
    else:
        print("Usage: roi_model.py --interactive | --input <file.json>")
        print("       roi_model.py --input <file.json> --format json")
        sys.exit(1)

    feature_name = inputs.get('feature_name', 'Feature')
    model_window = inputs.get('model_window_months', 12)
    time_to_impact = inputs.get('time_to_impact_months', 1)
    metric_type = inputs.get('metric_type', 'revenue')
    engineering_cost = inputs['engineering_cost']

    conservative = run_scenario(
        affected_population=inputs['affected_population'],
        lift=inputs['lift_conservative'],
        adoption_rate=inputs.get('adoption_rate', 1.0),
        revenue_per_unit=inputs['revenue_per_unit'],
        engineering_cost=engineering_cost,
        time_to_impact_months=time_to_impact,
        model_window_months=model_window,
        metric_type=metric_type,
    )

    base = run_scenario(
        affected_population=inputs['affected_population'],
        lift=inputs['lift_base'],
        adoption_rate=inputs.get('adoption_rate', 1.0),
        revenue_per_unit=inputs['revenue_per_unit'],
        engineering_cost=engineering_cost,
        time_to_impact_months=time_to_impact,
        model_window_months=model_window,
        metric_type=metric_type,
    )

    optimistic = run_scenario(
        affected_population=inputs['affected_population'],
        lift=inputs['lift_optimistic'],
        adoption_rate=inputs.get('adoption_rate', 1.0),
        revenue_per_unit=inputs['revenue_per_unit'],
        engineering_cost=engineering_cost,
        time_to_impact_months=time_to_impact,
        model_window_months=model_window,
        metric_type=metric_type,
    )

    if args.format == 'json':
        print(format_json_output(feature_name, inputs, conservative, base, optimistic))
    else:
        print(format_text_output(feature_name, inputs, conservative, base, optimistic))


if __name__ == '__main__':
    main()
