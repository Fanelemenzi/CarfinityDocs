# Insurance Claims Assessment Dashboard

## Dashboard Workflow Overview

### Primary User Journey
1. **Claims Table View** - Main dashboard with all claims in tabular format
2. **Claim Detail View** - Clicked claim expands to show full assessment information
3. **Component Assessment** - Detailed breakdown of each vehicle section with interactive elements


## 1. MAIN CLAIMS TABLE DASHBOARD

### Header Section
- **Company Logo & Branding**
- **Agent Profile**: John Smith | Senior Adjuster | Last Login: 2024-09-24 08:30
- **Quick Actions**: New Assessment | Advanced Search | Export Data | Settings
- **Notifications**: 🔔 (5) Priority alerts
- **Dashboard Stats Bar**: 42 Active | 15 Pending | 4.2h Avg Time | £1.2M Pipeline

### Claims Overview Table
```
╭─────────────────── ALL CLAIMS DASHBOARD ───────────────────╮
│                                                            │
│ Filters: [All Status ▼] [This Month ▼] [High Value ▼]     │
│ Search: [___________________________] 🔍                   │
│                                                            │
│┌────────────────────────────────────────────────────────┐ │
││ Showing 25 of 147 claims | Page 1 of 6    [◀] [▶]     ││ │
│└────────────────────────────────────────────────────────┘ │
│                                                            │
│┌─────┬───────────┬─────────────┬─────────┬──────┬────────┐ │
││ 🚨  │ CLAIM ID  │   VEHICLE   │  VALUE  │STATUS│ ACTION ││ │
│├─────┼───────────┼─────────────┼─────────┼──────┼────────┤ │
││ 🔴  │INS-8847   │2019 BMW 320i│ £35,000 │URGENT│[VIEW]  ││ │
││     │Sep 15     │VIN: WBA8E9G │Total Los│18h   │        ││ │
││     │Smith, J.  │             │         │      │        ││ │
│├─────┼───────────┼─────────────┼─────────┼──────┼────────┤ │
││ 🟡  │INS-8848   │2021 Audi A4 │ £12,500 │REVEW │[VIEW]  ││ │
││     │Sep 16     │VIN: WAUZZZF │Moderate │24h   │        ││ │
││     │Brown, M.  │             │         │      │        ││ │
│├─────┼───────────┼─────────────┼─────────┼──────┼────────┤ │
││ 🟢  │INS-8849   │2018 Ford    │ £4,200  │READY │[VIEW]  ││ │
││     │Sep 16     │Focus VIN:   │Minor    │2h    │        ││ │
││     │Davis, L.  │WF0AXXGCDA   │         │      │        ││ │
│├─────┼───────────┼─────────────┼─────────┼──────┼────────┤ │
││ 🔵  │INS-8850   │2020 Mercedes│ £18,900 │PROG  │[VIEW]  ││ │
││     │Sep 17     │C-Class VIN: │Major    │12h   │        ││ │
││     │Wilson, R. │WDD2053022A  │         │      │        ││ │
│├─────┼───────────┼─────────────┼─────────┼──────┼────────┤ │
││ 🟠  │INS-8851   │2017 VW Golf │ £8,750  │INFO  │[VIEW]  ││ │
││     │Sep 17     │VIN: WVWZZZ1K│Moderate │48h   │        ││ │
││     │Taylor, S. │             │         │      │        ││ │
└┴─────┴───────────┴─────────────┴─────────┴──────┴────────┘ │
│                                                            │
│ Status Legend:                                             │
│ 🔴 URGENT - Immediate attention required                   │
│ 🟡 REVIEW - Pending assessor review                       │  
│ 🟢 READY - Approved, ready for settlement                 │
│ 🔵 PROG - Assessment in progress                          │
│ 🟠 INFO - Additional information required                 │
│                                                            │
╰────────────────────────────────────────────────────────────╯
```

### Quick Stats Panel
```
┌─── TODAY'S METRICS ───┐  ┌─── PRIORITY QUEUE ───┐
│ New Claims:      8    │  │ SLA Risk:        5    │
│ Completed:      15    │  │ High Value:      3    │
│ In Progress:    23    │  │ Structural:      2    │
│ Avg Response:  4.2h   │  │ Fraud Flags:     1    │
└───────────────────────┘  └───────────────────────┘
```


## 2. CLAIM DETAIL VIEW (After Clicking [VIEW])

### Claim Header
```
╭─────────────────── CLAIM DETAILS: INS-8847 ────────────────────╮
│                                                                │
│ ← Back to Claims List                    Status: [IN PROGRESS] │
│                                                                │
│ Assessment ID: INS-2024-8847                                   │
│ ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ │
│ Vehicle: 2019 BMW 320i | VIN: WBA8E9G50KNU12345               │
│ Customer: John Smith | Policy: POL-789456123                  │
│ Incident: M25 Junction 15 | Date: 2024-09-15 14:30           │
│ Assessor: Sarah Johnson (Level 3) | Assigned: 2024-09-16      │
│                                                                │
│ 🚨 TOTAL LOSS CANDIDATE  🚨 STRUCTURAL DAMAGE  ⏰ 18h 42m SLA │
│                                                                │
╰────────────────────────────────────────────────────────────────╯
```

### Executive Summary Panel
```
╭─────────────────── ASSESSMENT SUMMARY ─────────────────────╮
│                                                            │
│ Overall Severity: ████████░░ 8/10 (Major Damage)          │
│ Estimated Cost:   £28,500 ± £3,200                        │
│ Market Value:     £18,750                                  │
│ Cost Ratio:       152% (Exceeds total loss threshold)     │
│                                                            │
│ UK Classification: Category S (Structural Damage)         │
│ SA 70% Rule:      ✓ EXCEEDED                              │
│ Recommendation:   TOTAL LOSS                              │
│                                                            │
│ Settlement Range: £16,200 - £18,750                       │
│                                                            │
╰────────────────────────────────────────────────────────────╯
```

### Vehicle Assessment Sections Navigation
```
╭─────────────────── DETAILED ASSESSMENT ───────────────────────╮
│                                                               │
│ Click any section below for detailed component breakdown:     │
│                                                               │
│ ┌─── ASSESSMENT SECTIONS ───────────────────────────────────┐ │
│ │                                                           │ │
│ │ 🚗 [EXTERIOR DAMAGE]     38/38 ✓  Severe      £15,200   │ │
│ │ 🛞 [WHEELS & TIRES]      12/12 ✓  Major        £3,800   │ │  
│ │ 🪑 [INTERIOR DAMAGE]     19/19 ✓  Moderate     £2,400   │ │
│ │ ⚙️  [MECHANICAL SYSTEMS] 18/20 ⚠️ Minor         £4,200   │ │
│ │ 🔌 [ELECTRICAL SYSTEMS]   9/9  ✓  Moderate     £1,900   │ │
│ │ 🛡️  [SAFETY SYSTEMS]      6/6  ✓  Major        £2,800   │ │
│ │ 🏗️  [FRAME & STRUCTURAL]  6/6  ✓  Severe       £8,400   │ │
│ │ 💧 [FLUID SYSTEMS]        6/6  ✓  Minor          £450   │ │
│ │ 📄 [DOCUMENTATION]        3/4  ⚠️ Complete        N/A    │ │
│ │                                                           │ │
│ │ Total Assessment Points: 117/120 Complete                │ │
│ │ Missing: Emissions sticker verification                   │ │
│ │                                                           │ │
│ └───────────────────────────────────────────────────────────┘ │
│                                                               │
╰───────────────────────────────────────────────────────────────╯
```

### Interactive Vehicle Damage Map
```
╭─────────────────── VEHICLE DAMAGE VISUALIZATION ──────────────────╮
│                                                                   │
│ Vehicle: 2019 BMW 320i | VIN: WBA8E9G50KNU12345                   │
│ Click on any highlighted area for detailed component assessment    │
│                                                                   │
│                    ┌── FRONT SECTION ──┐                         │
│                    │ ████████████████  │ 🔴 Severe Damage       │
│                 ┌──┤ Bumper  Grille    ├──┐                     │
│              ┌──┤  │ Hood    Lights    │  ├──┐                  │
│           ┌──┤ L  │ ████████████████  │  R ├──┐               │
│        ┌──┤ E  │  └───────────────────┘  I │ G├──┐            │
│     ┌──┤ F  │ F  │ ████████████████████ H │ H ├─┐├──┐         │
│  ┌──┤ T  │ R  │ R│ ████████████████████ T │ T │ E├─┐├──┐      │
│  │W │    │ O  │ O│ ████████████████████   │   │ A │ A├─┐│      │
│  │H │ S  │ N  │ N│ Side Panels & Doors   │   │ R │ R │W│      │
│  │E │ I  │ T  │ T│ ████████████████████   │   │   │   │H│      │
│  │E │ D  │    │  │ Rocker Panels         │   │   │   │E│      │
│  │L │ E  │ L  │ R│ ████████████████████   │   │ R │ L │E│      │
│  └──┤   │ E  │ I│ ████████████████████   │   │ I │   ├─┘│      │
│     └──┤ F  │ G│ ████████████████████   │ T │ G │ F ├──┘      │
│        └──┤ T  │ H│ ████████████████████ H │ T │ H ├──┘        │
│           └──┤   │ T│ ████████████████████T │   │ T├──┘         │
│              └──┤  │ └───────────────────┘  ├──┘               │
│                 └──┤ Rear Bumper  Lights ├──┘                 │
│                    │ ████████████████████ │ 🟡 Moderate       │
│                    └──── REAR SECTION ────┘                   │
│                                                                   │
│ Damage Legend:                                                    │
│ 🔴 Severe (Replace Required)    🟡 Moderate (Repair Required)     │
│ 🟠 Minor (Touch-up Required)    🟢 No Damage (Inspection Only)    │
│                                                                   │
│ ┌─── DAMAGE HOTSPOTS ───┐  ┌─── SECTION COSTS ───┐              │
│ │ 1. Front Impact Zone  │  │ Front End:    £8,350│              │
│ │    • Bumper System    │  │ Left Side:    £4,200│              │
│ │    • Headlight Assy   │  │ Right Side:   £2,850│              │
│ │    • Grille & Mount   │  │ Rear End:     £1,400│              │
│ │                       │  │ Structural:   £8,400│              │
│ │ 2. Left Side Impact   │  │ Interior:     £2,400│              │
│ │    • Door Damage      │  │ Mechanical:   £4,200│              │
│ │    • Panel Alignment  │  │ Electrical:   £1,900│              │
│ │                       │  │               ──────│              │
│ │ 3. Structural Damage  │  │ TOTAL:       £33,700│              │
│ │    • B-Pillar Shift   │  │                     │              │
│ │    • Frame Distortion │  │                     │              │
│ └───────────────────────┘  └─────────────────────┘              │
│                                                                   │
│ [View All Photos] [3D Inspection] [Print Diagram]                │
│                                                                   │
╰───────────────────────────────────────────────────────────────────╯
```

### Multi-Source Estimate Comparison
```
╭─────────────────── REPAIR ESTIMATE ANALYSIS ────────────────────╮
│                                                                 │
│ Multiple Estimates Retrieved: 5 sources analyzed               │
│ Recommended Estimate: Highlighted in GREEN                     │
│                                                                 │
│┌─────────────────────────────────────────────────────────────┐ │
││                 ESTIMATE COMPARISON TABLE                   ││ │
│├─────────────────┬────────────┬────────┬────────┬─────────────┤ │
││ SOURCE          │ TOTAL COST │ PARTS  │ LABOR  │ TIMELINE    ││ │
│├─────────────────┼────────────┼────────┼────────┼─────────────┤ │
││ 🔧 System Est   │   £28,500  │ £12,825│ £9,975 │  14 days    ││ │
││ 📋 Assessor     │   £31,200  │ £14,040│ £10,920│  18 days    ││ │
││ 🏢 BMW Dealer   │   £34,750  │ £17,375│ £12,775│  21 days    ││ │
││ ✅ Best Auto    │   £26,800  │ £11,740│ £9,380 │  16 days    ││ │
││ 🔧 QuickFix Ltd │   £29,100  │ £13,195│ £10,465│  15 days    ││ │
││ 🏆 Elite Repair │   £25,950  │ £11,200│ £8,850 │  12 days    ││ │
│├─────────────────┼────────────┼────────┼────────┼─────────────┤ │
││ 📊 AVERAGE      │   £29,383  │ £13,396│ £10,394│  16 days    ││ │
││ 📈 VARIANCE     │    ±£3,400 │  ±£2,588│ ±£1,725│   ±4 days   ││ │
│└─────────────────┴────────────┴────────┴────────┴─────────────┘ │
│                                                                 │
│ Detailed Cost Breakdown by Category:                           │
│ ┌─────────────────┬──────────┬──────────┬──────────┬──────────┐ │
│ │ REPAIR CATEGORY │  LOW EST │  HIGH EST│  AVERAGE │  RECOM   │ │
│ ├─────────────────┼──────────┼──────────┼──────────┼──────────┤ │
│ │ Body Panels     │   £8,200 │  £12,400 │  £10,100 │  £9,850  │ │
│ │ Paint & Finish  │   £3,100 │   £4,800 │   £3,950 │  £3,600  │ │
│ │ Structural      │   £7,800 │  £10,200 │   £8,900 │  £8,400  │ │
│ │ Mechanical      │   £3,900 │   £5,100 │   £4,450 │  £4,200  │ │
│ │ Electrical      │   £1,600 │   £2,400 │   £1,950 │  £1,900  │ │
│ │ Glass & Trim    │   £1,200 │   £1,850 │   £1,483 │  £1,350  │ │
│ └─────────────────┴──────────┴──────────┴──────────┴──────────┘ │
│                                                                 │
│ Quality Assessment:                                             │
│ ├─ Elite Repair: ⭐⭐⭐⭐⭐ (98% rating) - Recommended            │
│ ├─ Best Auto:    ⭐⭐⭐⭐⭐ (96% rating) - Good value            │
│ ├─ BMW Dealer:   ⭐⭐⭐⭐⭐ (99% rating) - Premium option        │
│ ├─ QuickFix Ltd: ⭐⭐⭐⭐░ (85% rating) - Budget option         │
│ └─ System Est:   ⭐⭐⭐⭐░ (AI Generated) - Baseline             │
│                                                                 │
│ [View Detailed Quotes] [Request New Estimate] [Select Provider] │
│                                                                 │
╰─────────────────────────────────────────────────────────────────╯
```

### Settlement Calculation Dashboard
```
╭─────────────────── SETTLEMENT CALCULATION CENTER ──────────────────╮
│                                                                    │
│ Claim: INS-8847 | Customer: John Smith | Policy: POL-789456123     │
│ Assessment Complete: ✓ | Estimates Reviewed: ✓ | Ready for Decision│
│                                                                    │
│ ┌──────────────── VEHICLE VALUATION ────────────────┐              │
│ │                                                   │              │
│ │ Market Value Sources:                             │              │
│ │ ├─ Glass Guide:        £18,750 (Primary)         │              │
│ │ ├─ AutoTrader:         £17,900 (Market avg)      │              │
│ │ ├─ CAP HPI:            £19,200 (Trade value)     │              │
│ │ ├─ Parkers Guide:      £18,400 (Consumer)        │              │
│ │ └─ Expert Valuation:   £18,650 (Professional)    │              │
│ │                                                   │              │
│ │ Agreed Market Value:   £18,750                    │              │
│ │ Pre-loss Condition:    Excellent (95% of book)   │              │
│ │                                                   │              │
│ └───────────────────────────────────────────────────┘              │
│                                                                    │
│ ┌──────────────── SETTLEMENT CALCULATIONS ──────────────────┐      │
│ │                                                           │      │
│ │ TOTAL LOSS SETTLEMENT:                                    │      │
│ │ ┌─────────────────────────────────────────────────────┐   │      │
│ │ │ Vehicle Agreed Value:           £18,750             │   │      │
│ │ │ Less: Policy Excess:              -£500             │   │      │
│ │ │ Less: Outstanding Finance:      -£12,400            │   │      │
│ │ │ Add: Salvage Recovery:           +£3,200            │   │      │
│ │ │ ─────────────────────────────────────────           │   │      │
│ │ │ Net Settlement to Customer:      £9,050             │   │      │
│ │ │                                                     │   │      │
│ │ │ Additional Considerations:                          │   │      │
│ │ │ • Personal effects allowance:     £250              │   │      │
│ │ │ • Key replacement:                £180              │   │      │
│ │ │ • Recovery costs covered          £0                │   │      │
│ │ │ ─────────────────────────────────────────           │   │      │
│ │ │ TOTAL CUSTOMER PAYMENT:          £9,480             │   │      │
│ │ └─────────────────────────────────────────────────────┘   │      │
│ │                                                           │      │
│ │ REPAIR SETTLEMENT (Alternative):                          │      │
│ │ ┌─────────────────────────────────────────────────────┐   │      │
│ │ │ Recommended Repair Cost:        £25,950             │   │      │
│ │ │ Less: Policy Excess:              -£500             │   │      │
│ │ │ Less: Betterment (10%):         -£2,595             │   │      │
│ │ │ Add: Rental Car (14 days):       +£420             │   │      │
│ │ │ ─────────────────────────────────────────           │   │      │
│ │ │ Total Repair Settlement:        £23,275             │   │      │
│ │ │                                                     │   │      │
│ │ │ Note: Repair exceeds 138% of value                 │   │      │
│ │ │ ❌ NOT ECONOMICALLY VIABLE                          │   │      │
│ │ └─────────────────────────────────────────────────────┘   │      │
│ │                                                           │      │
│ └───────────────────────────────────────────────────────────┘      │
│                                                                    │
│ ┌──────────────── FINANCIAL BREAKDOWN ──────────────────┐          │
│ │                                                       │          │
│ │ CLAIM COSTS TO INSURER:                              │          │
│ │ ├─ Customer Settlement:         £9,480               │          │
│ │ ├─ Assessment Costs:            £250                 │          │
│ │ ├─ Legal/Admin Fees:            £180                 │          │
│ │ ├─ Recovery Expenses:           £120                 │          │
│ │ └─ Less: Salvage Income:       -£3,200              │          │
│ │ ─────────────────────────────────────────            │          │
│ │ NET CLAIM COST:                £6,830                │          │
│ │                                                       │          │
│ │ RESERVE ADJUSTMENTS:                                 │          │
│ │ ├─ Original Reserve:            £25,000              │          │
│ │ ├─ Final Claim Cost:            £6,830               │          │
│ │ └─ Reserve Release:            +£18,170              │          │
│ │                                                       │          │
│ └───────────────────────────────────────────────────────┘          │
│                                                                    │
│ ┌──────────────── REGULATORY COMPLIANCE ──────────────────┐        │
│ │                                                         │        │
│ │ UK Requirements:                                        │        │
│ │ ☑ Category S Classification Applied                     │        │
│ │ ☑ DVLA Form V23 Ready for Submission                   │        │
│ │ ☑ HPI Database Update Scheduled                        │        │
│ │ ☐ Customer Notification Letter Generated              │        │
│ │                                                         │        │
│ │ South African Requirements (if applicable):            │        │
│ │ ☑ 70% Rule Assessment Complete (152% > 70%)            │        │
│ │ ☑ Total Loss Documentation Prepared                    │        │
│ │                                                         │        │
│ └─────────────────────────────────────────────────────────┘        │
│                                                                    │
│ ┌─────────────── SETTLEMENT AUTHORIZATION ───────────────┐         │
│ │                                                        │         │
│ │ Recommended Action: ✅ APPROVE TOTAL LOSS SETTLEMENT   │         │
│ │ Settlement Amount:  💷 £9,480                          │         │
│ │ Authority Level:    Senior Adjuster Required          │         │
│ │                                                        │         │
│ │ ┌────────────┐ ┌────────────┐ ┌─────────────┐        │         │
│ │ │ ✅ APPROVE │ │ ❌ REJECT  │ │ 🔍 REVIEW   │        │         │
│ │ │ Settlement │ │ & Revise   │ │ Further     │        │         │
│ │ └────────────┘ └────────────┘ └─────────────┘        │         │
│ │                                                        │         │
│ │ [Generate Settlement Letter] [Schedule Payment]       │         │
│ │ [Update Claim Status] [Notify All Parties]           │         │
│ │                                                        │         │
│ └────────────────────────────────────────────────────────┘         │
│                                                                    │
╰────────────────────────────────────────────────────────────────────╯
```

### Photo Gallery Overview
```
┌─── ASSESSMENT PHOTOS (47 total) ───┐
│                                    │
│ [IMG] [IMG] [IMG] [IMG] [IMG]      │
│ Overall  Damage Front  Rear  Side  │
│                                    │
│ [View All Photos] [Upload More]    │
└────────────────────────────────────┘
```


## 3. COMPONENT DETAIL VIEW (After Clicking Section)

### Section Header (Example: EXTERIOR DAMAGE clicked)
```
╭─────────────────── EXTERIOR DAMAGE ASSESSMENT ─────────────────────╮
│                                                                    │
│ ← Back to Claim Overview        Section: EXTERIOR BODY DAMAGE      │
│                                                                    │
│ Assessment Status: ✓ COMPLETE (38/38 points)                      │
│ Overall Severity: SEVERE                                           │
│ Section Cost: £15,200                                              │
│ Completion Date: 2024-09-16 15:30                                  │
│                                                                    │
╰────────────────────────────────────────────────────────────────────╯
```

### Detailed Component Assessment
```
╭───────────────── FRONT END ASSESSMENT (Points 1-10) ─────────────────╮
│                                                                      │
│ 1. Front Bumper                    [🔴 SEVERE]      £2,400          │
│    Structural damage, complete misalignment, sensor housing cracked  │
│    └─ Photos: [IMG_001] [IMG_002] [IMG_003] [View All]              │
│    └─ Assessment: REPLACE - OEM part required                       │
│    └─ Part #: BMW-51117379434 | Availability: 3-5 days             │
│    └─ Labor: 4.2 hours | Paint: Full front end blend               │
│                                                                      │
│ 2. Hood                           [🟡 MODERATE]     £850            │
│    Multiple impact dents, paint damage, minor alignment issues      │
│    └─ Photos: [IMG_004] [IMG_005] [View All]                       │
│    └─ Assessment: REPAIR - PDR and repaint                         │
│    └─ Labor: 6.5 hours | Materials: Filler, primer, paint          │
│                                                                      │
│ 3. Front Grille                   [🔴 SEVERE]      £320             │
│    Extensive cracks, missing pieces, mounting brackets damaged      │
│    └─ Photos: [IMG_006] [IMG_007]                                   │
│    └─ Assessment: REPLACE - Aftermarket acceptable                  │
│    └─ Part #: BMW-51117379435 | Availability: 1-2 days             │
│                                                                      │
│ 4. Headlight Housings             [🟡 MODERATE]    £650             │
│    Left housing cracked, moisture intrusion, mounting loose         │
│    └─ Photos: [IMG_008] [IMG_009]                                   │
│    └─ Assessment: REPLACE LEFT ONLY                                 │
│    └─ Part #: BMW-63117339901 | LED type, expensive                │
│                                                                      │
│ [Continue with remaining 6 components...]                           │
│                                                                      │
│ Section Totals:                                                     │
│ ├─ Parts Cost: £8,840                                               │
│ ├─ Labor Cost: £4,680 (26 hours @ £180/hr)                        │
│ ├─ Paint Cost: £1,680                                               │
│ └─ Total Section: £15,200                                           │
│                                                                      │
╰──────────────────────────────────────────────────────────────────────╯
```

### Side Panel Assessment (Points 11-20)
```
╭───────────────── SIDE PANEL ASSESSMENT (Points 11-20) ──────────────╮
│                                                                     │
│ 11. Driver Side Door              [🟡 MODERATE]    £1,200          │
│     Deep scratches, dent in center panel, handle scuffed           │
│     └─ Photos: [IMG_010] [IMG_011] [IMG_012]                       │
│     └─ Assessment: REPAIR - Fill, sand, repaint                    │
│     └─ Labor: 8 hours | Door blend required                        │
│                                                                     │
│ 12. Passenger Side Door           [🟢 MINOR]       £450            │
│     Light scratches, minor door handle damage                      │
│     └─ Photos: [IMG_013]                                           │
│     └─ Assessment: TOUCH-UP - Handle replacement                   │
│                                                                     │
│ [Continue with components 13-20...]                                │
│                                                                     │
╰─────────────────────────────────────────────────────────────────────╯
```

### Interactive Photo Viewer
```
┌─── COMPONENT PHOTO GALLERY ───┐
│                                │
│ Component: Front Bumper        │
│ ┌────────────────────────────┐ │
│ │                            │ │
│ │     [MAIN PHOTO VIEW]      │ │
│ │      IMG_001.jpg           │ │
│ │   Front bumper damage      │ │
│ │   Taken: 2024-09-16 10:30  │ │
│ │                            │ │
│ └────────────────────────────┘ │
│                                │
│ [◀ Prev] [1/3] [Next ▶]        │
│                                │
│ Thumbnails:                    │
│ [IMG1] [IMG2] [IMG3]           │
│                                │
│ [Download] [Annotate] [Share]  │
└────────────────────────────────┘
```


## 4. SECTION SUMMARY VIEW

### Assessment Progress Tracker
```
╭─────────────────── ASSESSMENT PROGRESS ───────────────────────╮
│                                                               │
│ Overall Completion: ████████████████████░ 97% (117/120)      │
│                                                               │
│ Section Breakdown:                                            │
│ ┌─────────────────┬──────┬────────────┬─────────┬──────────┐ │
│ │    SECTION      │ COMP │  SEVERITY  │  COST   │ STATUS   │ │
│ ├─────────────────┼──────┼────────────┼─────────┼──────────┤ │
│ │ Exterior Damage │38/38 │ Severe     │£15,200  │ ✓ Done   │ │
│ │ Wheels & Tires  │12/12 │ Major      │ £3,800  │ ✓ Done   │ │
│ │ Interior Damage │19/19 │ Moderate   │ £2,400  │ ✓ Done   │ │
│ │ Mechanical Sys  │18/20 │ Minor      │ £4,200  │ ⚠️ 90%   │ │
│ │ Electrical Sys  │ 9/9  │ Moderate   │ £1,900  │ ✓ Done   │ │
│ │ Safety Systems  │ 6/6  │ Major      │ £2,800  │ ✓ Done   │ │
│ │ Frame Struct    │ 6/6  │ Severe     │ £8,400  │ ✓ Done   │ │
│ │ Fluid Systems   │ 6/6  │ Minor      │  £450   │ ✓ Done   │ │
│ │ Documentation   │ 3/4  │ Complete   │   N/A   │ ⚠️ 75%   │ │
│ └─────────────────┴──────┴────────────┴─────────┴──────────┘ │
│                                                               │
│ Missing Items:                                                │
│ • Mechanical: Engine mount inspection pending                 │
│ • Mechanical: Brake line pressure test required              │
│ • Documentation: Emissions sticker verification              │
│                                                               │
╰───────────────────────────────────────────────────────────────╯
```


## 5. QUICK ACTIONS PANEL

### Decision Support Tools
```
╭─────────────────── CLAIM ACTIONS ───────────────────────╮
│                                                         │
│ Assessment Decision:                                    │
│ ┌─────────────┐ ┌─────────────┐ ┌─────────────┐      │
│ │ ✅ APPROVE   │ │ ❌ REJECT   │ │ 🔍 REQUEST  │      │
│ │ Total Loss  │ │ Assessment  │ │ More Info   │      │
│ └─────────────┘ └─────────────┘ └─────────────┘      │
│                                                         │
│ Settlement Actions:                                     │
│ ┌─────────────┐ ┌─────────────┐ ┌─────────────┐      │
│ │ £18,750     │ │ £16,200     │ │ CUSTOM      │      │
│ │ Market Val  │ │ Trade Val   │ │ Amount      │      │
│ └─────────────┘ └─────────────┘ └─────────────┘      │
│                                                         │
│ Communication:                                          │
│ ┌─────────────┐ ┌─────────────┐ ┌─────────────┐      │
│ │ 📞 CALL     │ │ 📧 EMAIL    │ │ 📄 GENERATE │      │
│ │ Customer    │ │ Summary     │ │ Report      │      │
│ └─────────────┘ └─────────────┘ └─────────────┘      │
│                                                         │
╰─────────────────────────────────────────────────────────╯
```


## 6. MOBILE VIEW ADAPTATIONS

### Mobile Claims Table
```
┌─── MOBILE CLAIMS VIEW ───┐
│ ☰ Menu      🔔(5)    👤  │
├───────────────────────────┤
│                           │
│ 🔍 Search claims...       │
│ [All Status ▼] [Filter]   │
│                           │
│ ┌───── INS-8847 ─────┐   │
│ │🔴 URGENT | £35,000  │   │
│ │2019 BMW 320i       │   │
│ │Smith, J. | 18h SLA  │   │
│ │[VIEW DETAILS]       │   │
│ └─────────────────────┘   │
│                           │
│ ┌───── INS-8848 ─────┐   │
│ │🟡 REVIEW | £12,500  │   │
│ │2021 Audi A4        │   │
│ │Brown, M. | 24h SLA  │   │
│ │[VIEW DETAILS]       │   │
│ └─────────────────────┘   │
│                           │
│ [Load More Claims]        │
│                           │
└───────────────────────────┘
```

### Mobile Component View
```
┌─── COMPONENT DETAILS ────┐
│ ← Back    Front Bumper    │
├───────────────────────────┤
│                           │
│ Status: 🔴 SEVERE         │
│ Cost: £2,400              │
│                           │
│ ┌─── Photo Gallery ───┐  │
│ │ [Swipe for more]     │  │
│ │ ┌─────────────────┐  │  │
│ │ │                 │  │  │
│ │ │   Photo 1/3     │  │  │
│ │ │                 │  │  │
│ │ └─────────────────┘  │  │
│ │ ● ○ ○               │  │
│ └─────────────────────┘  │
│                           │
│ Assessment Notes:         │
│ "Structural damage,       │
│ complete misalignment,    │
│ sensor housing cracked"   │
│                           │
│ Recommendation: REPLACE   │
│ Part #: BMW-51117379434   │
│ Availability: 3-5 days    │
│                           │
│ [Approve] [Request Info]  │
│                           │
└───────────────────────────┘
```


## Navigation Flow Summary

### User Journey Map
```
Main Claims Table
       │
       ▼ (Click [VIEW])
Claim Detail View
       │
       ▼ (Click Section)
Component Assessment
       │
       ▼ (Click Component)
Detailed Component View
       │
       ▼ (Actions)
Decision/Settlement
```

### Key Features
- **Responsive Design**: Seamless desktop to mobile experience
- **Progressive Disclosure**: Information revealed as needed
- **Quick Actions**: One-click approvals and decisions
- **Visual Indicators**: Color coding and status symbols throughout
- **Photo Integration**: Contextual image viewing at every level
- **Real-time Updates**: Live status changes and notifications

This workflow-based design ensures insurance claims agents can efficiently process claims from high-level overview to detailed component analysis, with all necessary decision-making tools accessible at the appropriate level of detail.