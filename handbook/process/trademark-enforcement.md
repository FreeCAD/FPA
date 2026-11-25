---
title: "Trademark enforcement"
description:
    "The procedure that the FPA uses when a third party infringes the FreeCAD trademarks."
layout: default
---

# {{page.title}}

{{page.description}}

## Purpose

The FPA owns the FreeCAD trademarks and must protect them.
The trademarks tell users that software comes from the FreeCAD project.
If the FPA knows of an infringement and does not act, it can lose some of its rights.
Thus the FPA sends a written notice to each third party that infringes the trademarks.
The FPA also keeps a record of each action, as evidence that it protects its rights.

This page is not legal advice.
If a case is not clear, get advice from a lawyer.

## The trademarks

| Registration number | Mark | Office | Registered | Expires | Goods (class 9) | Documents |
|:--|:--|:--|:--|:--|:--|:--|
| 1514682 | Current FreeCAD logo, figurative mark with the word element "FreeCAD" | BOIP (Benelux) | 2025-01-31 | 2034-11-21 | CAD, CAM, CAE, civil engineering, and 3D computer graphics software | [Register copy](../../documents/Trademark%20-%20new%20logo.pdf), [certificate](../../documents/Trademark%20certificate%20-%20new%20logo.pdf) |
| 1466186 | Old FreeCAD logo, figurative mark with the word element "FreeCAD" | BOIP (Benelux) | 2022-10-04 | 2032-06-20 | CAD software | [Register copy](../../documents/Trademark%20-%20old%20logo.pdf), [certificate](../../documents/Trademark%20certificate%20-%20old%20logo.pdf) |

The two registrations apply in Belgium, the Netherlands, and Luxembourg.
In other countries, the FPA can ask for compliance, but the registrations give fewer legal rights.

When the FPA gets a new registration, add it to this table and to the letter template.

## Files

| Item | Location | Access |
|:--|:--|:--|
| Letter template | [`documents/templates/trademark infringement notice.md`](../../documents/templates/trademark%20infringement%20notice.md) | Public |
| Enforcement log | `encrypted/trademark/enforcement-log.md` | FPA members with the encryption key |
| Evidence | `encrypted/trademark/evidence/[CASE ID]/` | FPA members with the encryption key |
| Copies of letters that the FPA sent | `encrypted/letters/` | FPA members with the encryption key |
| Letters that the FPA received | `encrypted/letters/received/` | FPA members with the encryption key |

The log and the letters are not public.
They contain names of third parties and statements that are not proved.

## Roles

| Role | Responsibility |
|:--|:--|
| Case owner | An FPA member who collects the evidence, writes the letter, and updates the log. |
| Administrative body | Approves each formal notice and each escalation. |
| Chairperson | Signs the formal notice. The chairperson can give this task to a different administrator. |

## Is the use an infringement?

Compare the use with the [brand guidelines](./logo.md).

These uses are usually an infringement:

- A modified version of FreeCAD that a third party distributes with the FreeCAD name or logo.
- A website that is not `freecad.org` and distributes installers with the FreeCAD name or logo. This is more serious if the installer contains added software.
- A domain name, store entry, or social media account that contains "FreeCAD" and looks official.
- A product or service with "FreeCAD" in its name, if the name suggests that the FPA made or approved it.
- Goods for sale that show the FreeCAD logo without permission.
- A changed version of the FreeCAD logo.

These uses are usually not an infringement:

- A book, course, video, or article that refers to FreeCAD by name.
- A statement of fact, for example "based on FreeCAD" or "for use with FreeCAD".
- A package of unmodified FreeCAD that obeys the brand guidelines, for example a Linux distribution package.
- The logo as a credit or as a link to `freecad.org`.

## Procedure

### 1. Record the report

1. Send each report of possible infringement to <fpa@freecad.org>.
2. Give the case to a case owner.
3. Open a new case in the enforcement log.
4. Give the case an ID in the format `TM-YYYY-NN`.

### 2. Collect the evidence

1. Make screen captures that show the use, the URL, and the date.
2. Save the pages in a public web archive, if possible.
3. Find the name and the contact data of the third party.
4. Find the hosting provider, the domain registrar, or the platform.
5. Save all evidence in `encrypted/trademark/evidence/[CASE ID]/`.
6. Record the evidence in the log.

Collect the evidence before you contact the third party.
The third party can remove the content after the first contact.

### 3. Make a decision

1. Give the administrative body a summary of the case and the evidence.
2. The administrative body selects one of these decisions:
   - No infringement. Close the case.
   - Informal contact first.
   - Formal notice.
3. Record the decision in the log.

Use an informal contact when the third party is a community member or the error is clearly not intentional.
A short, friendly message is frequently sufficient.
If the informal contact gets no result in 14 days, send the formal notice.

### 4. Send the formal notice

1. Copy the letter template.
2. Complete all fields. Set the deadline to 14 days after the date of the letter.
3. Make sure that each statement in the letter is correct and that the evidence shows it.
4. Get approval from the administrative body.
5. Get the signature of the chairperson.
6. Export the letter to PDF.
7. Send the PDF by email from <fpa@freecad.org>.
8. If you know the postal address and the case is serious, also send the letter by registered mail.
9. Save the PDF as `encrypted/letters/YYYY.MM.DD Trademark notice - [PARTY].pdf`.
10. Record the action and the deadline in the log.

**CAUTION: Do not make public statements about an open case. A public accusation that is not correct can cause legal risk for the FPA.**

### 5. Monitor the response

1. Examine the use again on the deadline date.
2. Save each answer from the third party in `encrypted/letters/received/`.
3. Record the answer and the result of the check in the log.
4. If the third party stopped the use, go to step 7.
5. If the third party disagrees, give the answer to the administrative body for a decision.
6. If there is no answer and the use continues, send a second notice with a deadline of 7 days.

### 6. Escalate

If the use continues after the second deadline, the administrative body selects the next action.
Possible actions are:

- A trademark report to the hosting provider or the domain registrar.
- A trademark report to the store, marketplace, or social media platform.
- A domain name dispute (UDRP) for a domain name that contains "FreeCAD".
- Advice from a lawyer, and legal action if necessary.

Record each action in the log.
The FPA spending rules apply to all costs.

### 7. Close the case

1. Make a screen capture that shows that the use stopped.
2. Record the result and the close date in the log.
3. Set the case status to "Resolved" or "Closed, no action".
4. Examine the location again after 3 months. Record this check in the log.

## Maintenance of the log

- Update the log on the same day as each action.
- Do not delete old entries.
- The administrative body examines all open cases one time each quarter.
