# Formula Details

## Core Components

### 1. Basic Premium Calculation
- **Formula**: Basic Premium = Sum Insured × Rate
- **Description**: Direct multiplication of the sum insured amount by the premium rate
- **Note**: The rate is used as a decimal multiplier, not as a percentage
- **Example**: Sum Insured of 1,000,000 with rate 0.02 gives Basic Premium of 20,000

### 2. Administrative Charges
- **Formula**: Administrative Charges = Min(5% of Basic Premium, 5000)
- **Description**: Administrative charges are calculated as 5% of the basic premium but capped at 5000 Rs
- **Logic**:
  - Calculate 5% of Basic Premium
  - If 5% of Basic Premium > 5000, use 5000
  - If 5% of Basic Premium ≤ 5000, use the calculated 5% value
- **Purpose**: Ensures administrative charges don't exceed 5000 Rs

### 3. Subtotal
- **Formula**: Subtotal = Basic Premium + Administrative Charges
- **Description**: The combined amount after adding administrative charges to the basic premium
- **Usage**: Forms the basis for federal surcharge and stamp duty calculations

### 4. Federal Surcharge
- **Formula (Punjab)**: Federal Surcharge = Subtotal × 0.16
- **Formula (Sindh)**: Federal Surcharge = Subtotal × 0.15
- **Description**: Provincial surcharge that varies by location
- **Rates**:
  - Punjab: 16% of subtotal
  - Sindh: 15% of subtotal
- **Purpose**: Government surcharge that differs by province

### 5. Stamp Duty
- **Formula**: Stamp Duty = Subtotal × 0.01
- **Description**: Fixed 1% charge applied to the subtotal
- **Purpose**: Government stamp duty requirement

### 6. Stamp Charges
- **Formula**: Stamp Charges = Variable amount specified by user
- **Description**: Case-specific charges that vary per transaction
- **Common Values**: Typically Rs 10, 20, or 50
- **Purpose**: Actual stamp charges that differ by specific case requirements

### 7. Net Premium
- **Formula**: Net Premium = Subtotal + Federal Surcharge + Stamp Duty + Stamp Charges
- **Description**: The final total premium amount including all charges
- **Purpose**: Total amount payable by the insured party

## Calculation Sequence
1. Calculate Basic Premium
2. Calculate Administrative Charges (apply cap if needed)
3. Calculate Subtotal
4. Calculate Federal Surcharge (based on province)
5. Calculate Stamp Duty
6. Add Stamp Charges
7. Calculate Net Premium

## Validation Rules
- Sum Insured must be greater than 0
- Rate must be greater than 0
- Stamp Charges cannot be negative
- Province must be either 'Punjab' or 'Sindh'

## Edge Cases
- When Basic Premium is low, administrative charges may equal 5% of Basic Premium
- When Basic Premium is high, administrative charges will be capped at 5000
- Federal surcharge varies significantly between provinces (16% vs 15%)