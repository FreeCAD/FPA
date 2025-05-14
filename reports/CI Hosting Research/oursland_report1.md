# FreeCAD CI Hosting Research Report

This report (WIP) documents the costs associated with FreeCAD continuous integration (CI) currently borne by GitHub, different approaches for self-hosting the GitHub CI runners, and their costs.

## Current Utilization on Azure

This chapter outlines the resource utilization on the GitHub-hosted runners as well as an estimate of what the equivalent costs would be if FreeCAD were to pay out of pocket.  The cost estimate approach is to estimate monthly utilization and to price out the equivalent utilization on the Microsoft Azure servers that were utilized by GitHub.  No costs associated with maintenance or scalability is considered.

### FreeCAD Utilization Data (Feb 14, 2025 to March 16, 2025)

The following values were pulled from GitHub's Insights into Action Usage Metrics for the FreeCAD main repository.

Total minutes: 235,404
Total job runs: 12,268
Avg job run time: 18m 32s
Avg job queue time: 12m 50s
Job failure rate: 5%
Failed job usage: 12,686 minutes

| OS      | Total Minutes | Workflow Runs |
| ------- | ------------- | ------------- |
| windows | 123,450       | 1,350         |
| linux   | 85,808        | 3,000         |
| macos   | 26,146        | 1,342         |

![[minutes over time.png]]

![[workflow runs over time.png]]

Examining the maximum utilization of each OS, we arrive at the following:

| OS      | Monthly Minutes | Monthly Hours | Monthly Instances |
| ------- | --------------- | ------------- | ----------------- |
| Windows | 98453           | 1641          | 3                 |
| Linux   | 124373          | 2073          | 3                 |
| macOS   | 22130           | 369           | 1                 |

### Current Standard GitHub-hosted runners

#### Burstable (Cost Optimized)

| **Virtual Machine**    | **Processor (CPU)** | **Memory (RAM)** | **Storage (SSD)** | **Architecture** | Azure        | AWS                  | Google         | MacStadium    |
| ---------------------- | ------------------- | ---------------- | ----------------- | ---------------- | ------------ | -------------------- | -------------- | ------------- |
| Linux                  | 4                   | 16 GB            | 14 GB             | x64              | B4ms/B4as_v2 | t3.xlarge/t3a.xlarge | e2-standard-4  |               |
| Windows                | 4                   | 16 GB            | 14 GB             | x64              | B4ms/B4as_v2 | t3.xlarge/t3a.xlarge | e2-standard-4  |               |
| Linux [Public preview] | 4                   | 16 GB            | 14 GB             | arm64            | B4ps_v2      | t4g.xlarge           | t2a-standard-4 |               |
| macOS                  | 3 (M1)              | 7 GB             | 14 GB             | arm64            |              | mac2.metal           |                | M4.S Mac Mini |

#### Standard

| **Virtual Machine**    | **Processor (CPU)** | **Memory (RAM)** | **Storage (SSD)** | **Architecture** | Azure   | AWS                  | Google         | MacStadium    |
| ---------------------- | ------------------- | ---------------- | ----------------- | ---------------- | ------- | -------------------- | -------------- | ------------- |
| Linux                  | 4                   | 16 GB            | 14 GB             | x64              | D4as_v4 | t3.xlarge/t3a.xlarge | t2d-standard-4 |               |
| Windows                | 4                   | 16 GB            | 14 GB             | x64              | D4as_v4 | t3.xlarge/t3a.xlarge | t2d-standard-4 |               |
| Linux [Public preview] | 4                   | 16 GB            | 14 GB             | arm64            | D4ps_v6 | t4g.xlarge           | t2a-standard-4 |               |
| macOS                  | 3 (M1)              | 7 GB             | 14 GB             | arm64            |         | mac2.metal           |                | M4.S Mac Mini |

### Cost Estimates (Monthly)

GitHub, as a Microsoft company, utilizes Azure for cloud hosting.  Unfortunately, neither Azure nor Google provide Apple macOS hosts, so MacStadium's pricing is substituted.

Assumption: CI usage is uniformly distributed and consequently providing excess CI availability is sufficient to satisfy the requirements.  As this is not actually the case, the following values represent a bare minimum for cost estimates but not necessarily an ideal.

#### Azure

* Cost Optimized:

| **OS**  | Description        | Cost    |
| ------- | ------------------ | ------- |
| Linux   | (3x) B4as v2       | $328.50 |
| Windows | (3x) B4as v2       | $419.62 |
| macOS   | (1x) M4.S Mac Mini | $119.00 |
| TOTAL   |                    | $867.12 |

* Standard:

| **OS**  | Description        | Cost     |
| ------- | ------------------ | -------- |
| Linux   | (3x) D4as v4       | $430.08  |
| Windows | (3x) D4as v4       | $896.57  |
| macOS   | (1x) M4.S Mac Mini | $119.00  |
| TOTAL   |                    | $1445.65 |

#### AWS

For comparison, equivalent runners on AWS, each with 32 GiB of EBS would cost:

* Cost Optimized

| OS      | Description     | Cost     |
| ------- | --------------- | -------- |
| Linux   | (3x) t3a.xlarge | $337.06  |
| Windows | (3x) t3a.xlarge | $498.24  |
| macOS   | (1x) mac2       | $477.70  |
| TOTAL   |                 | $1313.00 |

* Standard

| OS      | Description    | Cost     |
| ------- | -------------- | -------- |
| Linux   | (3x) t3.xlarge | $393.78  |
| Windows | (3x) t3.xlarge | $2014.96 |
| macOS   | (1x) mac2      | $477.70  |
| TOTAL   |                | $2886.44 |

#### Google

* Cost Optimized

| **OS**  | Description         | Cost    |
| ------- | ------------------- | ------- |
| Linux   | (3x) t2d-standard-4 | $60.07  |
| Windows | (3x) t2d-standard-4 | $463.03 |
| macOS   | (1x) M4.S Mac Mini  | $119.00 |
| TOTAL   |                     | $642.10 |

* Standard

| **OS**  | Description        | Cost    |
| ------- | ------------------ | ------- |
| Linux   | (3x) e2-standard-4 | $133.67 |
| Windows | (3x) e2-standard-4 | $536.63 |
| macOS   | (1x) M4.S Mac Mini | $119.00 |
| TOTAL   |                    | $789.30 |
