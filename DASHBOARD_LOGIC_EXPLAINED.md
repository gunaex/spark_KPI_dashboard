# Dashboard Logic & AI Intelligence Documentation

This document outlines the visual architecture and algorithmic "intelligence" (AI Logic) behind the SPARK Executive KPI Dashboards.

---

## 1. Visualization Logic Architecture

### Technology Stack
- **Frontend Core:** HTML5, CSS3 (Custom Design System).
- **Charting Engine:** [Chart.js](https://www.chartjs.org/) with `chartjs-plugin-datalabels` for interactive annotations.
- **Data Engine:** [SheetJS (XLSX.js)](https://sheetjs.com/) for client-side Excel processing.

### Design System: "Blue Earthtone"
The dashboard utilizes a curated color palette designed for high-contrast executive readability:
- **Olive (`#558B2F`):** Success / Normal status.
- **Rust (`#BF360C`):** Delay / Critical risk.
- **Taupe (`#8D6E63`):** Neutral / Trend baseline.
- **Blue Earth (`#2E5A88`):** Informational / Stage distribution.
- **Header Espresso (`#4E342E`):** Structural grounding.

### Visual Components & Data Mapping
| Chart Component | Visualization Type | Data Logic |
| :--- | :--- | :--- |
| **Overall Health** | Doughnut | Aggregates project count by `SLA Status`. Visualizes strictly Normal vs. Delayed proportions. |
| **Current Pipeline** | Horizontal Bar | Categorizes projects by their current lifecycle stage (e.g., REQ, SOL, IMP). |
| **Section Efficiency** | Horizontal Bar | Calculates efficiency using a **100% Baseline Logic**: `100 + ((Days Saved / Total SLA) * 100)`. Includes day-saved annotations. |
| **Milestone Ranking** | Stacked Bar | Shows the distribution of Advance/Normal/Delay counts across 9 PMO Phases. |
| **Variance Analysis** | Waterfall-style Bar | Displays the average deviation in days (+/-) per stage for bottleneck identification. |
| **Milestone Reliability**| Radar | Shows the "Success %" (Advance + Normal / Total) for each stage to detect consistency gaps. |
| **Team Distribution** | Stacked Bar | Maps performance (Late vs. OK) directly to specific engineering/ITO teams. |

---

## 2. AI & Intelligence Logic (Executive Summary)

The dashboard features a **Heuristic AI Engine** that translates raw project data into actionable executive insights.

### Heuristic Analysis Functions
Whenever a new Excel file is uploaded, the script runs the following logic:

1.  **Stage Comparison Algorithm:**
    - Compares `Advance + Normal` ratios across all 9 milestones.
    - Identifies the **Best Milestone** (Highest reliability %).
    - Identifies the **Worst Milestone** (Highest delay frequency).

2.  **Friction Point Detection:**
    - Scans `actual` vs `target` dates to find the maximum variance.
    - Identifies the specific stage causing the most significant "Portfolio Friction."

3.  **Dynamic Executive Note Generation:**
    - **Pros Generation:** Automatically credits the "Best Stage" and highlights the number of projects delivered ahead of schedule.
    - **Cons Generation:** Flagging the total count of delayed projects and specifically naming the "Worst Stage" with the `Max Delay` value.
    - **Summary Statement:** Calculates the overall portfolio stability percentage and suggests where performance recovery plans should be focused.

### Example AI Output Transformation:
> *Raw Data:* REQ-C has 90% on-time, HO-DEV has 40% delays with one project 15 days late.
> 
> **AI Logic Output:**
> - **Pros:** High stability in **REQ-C** (90% reliability).
> - **Cons:** Found 10 projects delayed. Friction point identified in **HO-DEV** stage (Max Delay: 15 days).
> - **Summary:** SPARK is currently managing a 60% stable portfolio. Performance recovery plans focused on HO-DEV are underway.

---

## 3. SLA & Phase Logic

The system follows a strict 9-phase PMO lifecycle with predefined SLAs:

1.  **REQ-C:1D** (Requirement Gathering: 1 Day SLA)
2.  **SOL-BUD:14D** (Solution and Budgetary: 14 Day SLA)
3.  **PROP-RQ:3D** (Proposal/PR&PO: 3 Day SLA)
4.  **IMP-VOB:14D** (Vendor Onboarding: 14 Day SLA)
5.  **IMP-SEC:14D** (Security: 14 Day SLA)
6.  **HO-INST-DEV:1D** (Install Dev: 1 Day SLA)
7.  **HO-DEV:1D** (Sign off H/O Dev: 1 Day SLA)
8.  **HO-INST-PROD:1D** (Install Prod: 1 Day SLA)
9.  **HO-PROD:1D** (Sign off H/O Prod: 1 Day SLA)

### Status Calculation:
- **Advance:** `Actual Date < Target Date`
- **Normal:** `Actual Date == Target Date`
- **Delay:** `Actual Date > Target Date`
- **Efficiency Score:** `(Target - Actual)` / `(Target - Start)` base weighted.
