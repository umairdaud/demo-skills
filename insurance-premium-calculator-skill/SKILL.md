---
name: Insurance Premium Calculator
description: Calculate net premiums for engineering policies including Contractors All Risk, Erection Policy, and Machinery policies. Use when Claude needs to compute insurance premiums based on sum insured, rate, province, and various charges including administrative fees, federal surcharges, stamp duties, and stamp charges.
---

# Insurance Premium Calculator Skill

## Overview
This skill calculates net premiums for engineering insurance policies including Contractors All Risk, Erection Policy, and Machinery policies. It implements the complete premium calculation formula with all required components.

## When to Use This Skill
- Calculating insurance premiums for engineering policies
- Computing net premium based on sum insured and rate
- Applying administrative charges with 5% calculation capped at Rs 5000
- Calculating federal surcharges (16% for Punjab, 15% for Sindh)
- Applying stamp duty (1% of subtotal)
- Including variable stamp charges

## Inputs Required
- Sum Insured: The amount to be insured
- Rate: The premium rate (used directly as multiplier, not percentage)
- Province: Punjab or Sindh (affects federal surcharge rate)
- Stamp Charges: Variable amount for stamp charges (typically Rs 10, Rs 20, or Rs 50)

## Calculation Formula

### 1. Basic Premium
- Formula: (Sum Insured × Rate) ÷ 100
- Description: Multiplication of sum insured by the rate, then divided by 100

### 2. Administrative Charges
- Formula: Min(5% of Basic Premium, 5000)
- Description: 5% of basic premium with a maximum cap of Rs 5000
- Logic: If 5% of Basic Premium > 5000, use 5000; otherwise use calculated 5%

### 3. Subtotal
- Formula: Basic Premium + Administrative Charges
- Description: Combined amount after adding admin charges to basic premium

### 4. Federal Surcharge
- Punjab: 16% of Subtotal
- Sindh: 15% of Subtotal
- Description: Provincial surcharge based on location

### 5. Stamp Duty
- Formula: 1% of Subtotal
- Description: Fixed 1% charge on the subtotal

### 6. Net Premium
- Formula: Subtotal + Federal Surcharge + Stamp Duty + Stamp Charges
- Description: Final total premium amount

## Execution Steps
1. Prepare input values (sum insured, rate, province, stamp charges)
2. Execute the premium calculation script
3. Review the detailed breakdown of all calculations
4. Verify the net premium amount

## Reference Materials
See references/calculation_examples.md for detailed calculation examples and references/formula_details.md for comprehensive formula documentation.

## Quality Standards
- Always provide a detailed breakdown of all calculations
- Format monetary amounts with appropriate precision
- Validate inputs before performing calculations
- Include provincial differences in federal surcharge rates
- Clearly indicate the capping mechanism for administrative charges