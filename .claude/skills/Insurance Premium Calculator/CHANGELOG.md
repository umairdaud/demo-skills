# Changelog
All notable changes to the Insurance Premium Calculator skill will be documented in this file.

## [Unreleased] - 2026-01-11

### Added
- New example demonstrating administrative charge capping scenario (Example 4)

### Changed
- Updated Basic Premium calculation formula to divide by 100: `(Sum Insured × Rate) ÷ 100`
- Updated all calculation examples to reflect the new formula
- Moved currency indicator "Rs" to before all monetary values instead of after
- Updated administrative charge capping example to show proper comparison (10,000 > 5000)

### Fixed
- Corrected mathematical comparison in administrative charge logic documentation
- Ensured all monetary values consistently show "Rs" before the amount

### Security
- No security-related changes

## [Initial Release] - 2025-12-XX

### Added
- Insurance Premium Calculator skill for engineering policies
- Support for Contractors All Risk, Erection Policy, and Machinery policies
- Calculation of basic premium, administrative charges, federal surcharges, and stamp duties
- Support for Punjab and Sindh provinces with different federal surcharge rates
- Administrative charge capping mechanism (max Rs 5000)
- Command-line interface for premium calculations