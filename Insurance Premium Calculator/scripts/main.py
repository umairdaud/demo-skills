#!/usr/bin/env python3
"""
Insurance Premium Calculator for Engineering Policies
Calculates net premium for Contractors All Risk, Erection Policy, and Machinery policies
"""

import argparse
import sys


def calculate_basic_premium(sum_insured, rate):
    """
    Calculate basic premium: (Sum Insured * Rate) / 100

    Args:
        sum_insured (float): The sum insured amount
        rate (float): The premium rate (not as percentage)

    Returns:
        float: Basic premium amount
    """
    return (sum_insured * rate) / 100


def calculate_administrative_charges(basic_premium):
    """
    Calculate administrative charges: min(5% of basic premium, 5000)
    If 5% of basic premium > 5000, use 5000
    If 5% of basic premium < 5000, use the calculated 5% value

    Args:
        basic_premium (float): The basic premium calculated

    Returns:
        float: Administrative charges amount
    """
    five_percent = basic_premium * 0.05
    # Cap the administrative charges at 5000
    return min(five_percent, 5000)


def calculate_federal_surcharge(subtotal, province):
    """
    Calculate federal surcharge: 16% for Punjab, 15% for Sindh

    Args:
        subtotal (float): Subtotal after adding admin charges
        province (str): Province (Punjab or Sindh)

    Returns:
        float: Federal surcharge amount
    """
    if province.lower() == 'punjab':
        return subtotal * 0.16
    elif province.lower() == 'sindh':
        return subtotal * 0.15
    else:
        raise ValueError("Province must be either 'Punjab' or 'Sindh'")


def calculate_stamp_duty(subtotal):
    """
    Calculate stamp duty: 1% of subtotal

    Args:
        subtotal (float): Subtotal after adding admin charges

    Returns:
        float: Stamp duty amount
    """
    return subtotal * 0.01


def calculate_net_premium(sum_insured, rate, province, stamp_charges):
    """
    Calculate net premium for engineering policies

    Args:
        sum_insured (float): The sum insured amount
        rate (float): The premium rate percentage
        province (str): Province (Punjab or Sindh)
        stamp_charges (float): Stamp charges amount

    Returns:
        dict: Detailed breakdown of the calculation
    """
    basic_premium = calculate_basic_premium(sum_insured, rate)
    administrative_charges = calculate_administrative_charges(basic_premium)

    # Subtotal after adding admin charges to basic premium
    subtotal = basic_premium + administrative_charges

    # Calculate federal surcharge based on province
    federal_surcharge = calculate_federal_surcharge(subtotal, province)

    # Calculate stamp duty
    stamp_duty = calculate_stamp_duty(subtotal)

    # Net premium = subtotal + federal surcharge + stamp duty + stamp charges
    net_premium = subtotal + federal_surcharge + stamp_duty + stamp_charges

    return {
        'sum_insured': sum_insured,
        'rate': rate,
        'province': province,
        'basic_premium': basic_premium,
        'administrative_charges': administrative_charges,
        'subtotal': subtotal,  # Basic premium + admin charges
        'federal_surcharge': federal_surcharge,
        'stamp_duty': stamp_duty,
        'stamp_charges': stamp_charges,
        'net_premium': net_premium
    }


def main():
    parser = argparse.ArgumentParser(description='Calculate insurance premium for engineering policies')
    parser.add_argument('--sum-insured', '-s', type=float, required=True,
                        help='Sum insured amount')
    parser.add_argument('--rate', '-r', type=float, required=True,
                        help='Premium rate percentage')
    parser.add_argument('--province', '-p', type=str, required=True,
                        choices=['Punjab', 'Sindh', 'punjab', 'sindh'],
                        help='Province (Punjab or Sindh)')
    parser.add_argument('--stamp-charges', '-sc', type=float, required=True,
                        help='Stamp charges amount (typically Rs 10, 20, or 50)')

    args = parser.parse_args()

    # Validate inputs
    if args.sum_insured <= 0:
        print("Error: Sum insured must be greater than 0", file=sys.stderr)
        sys.exit(1)

    if args.rate <= 0:
        print("Error: Rate must be greater than 0", file=sys.stderr)
        sys.exit(1)

    if args.stamp_charges < 0:
        print("Error: Stamp charges cannot be negative", file=sys.stderr)
        sys.exit(1)

    # Calculate the premium
    result = calculate_net_premium(args.sum_insured, args.rate, args.province, args.stamp_charges)

    # Display results
    print("Insurance Premium Calculation Breakdown")
    print("=" * 50)
    print(f"Sum Insured:        Rs {result['sum_insured']:,.2f}")
    print(f"Rate:               {result['rate']:.4f}")  # Show as decimal, not percentage
    print(f"Basic Premium:      Rs {result['basic_premium']:,.2f}")
    print(f"Admin Charges:      Rs {result['administrative_charges']:,.2f}")
    print("-" * 50)
    print(f"Subtotal:           Rs {result['subtotal']:,.2f}")
    print(f"Federal Surcharge:  Rs {result['federal_surcharge']:,.2f} ({'16%' if result['province'].lower() == 'punjab' else '15%'} of subtotal)")
    print(f"Stamp Duty:         Rs {result['stamp_duty']:,.2f} (1% of subtotal)")
    print(f"Stamp Charges:      Rs {result['stamp_charges']:,.2f}")
    print("-" * 50)
    print(f"Net Premium:        Rs {result['net_premium']:,.2f}")


if __name__ == "__main__":
    main()