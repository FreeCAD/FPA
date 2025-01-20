---
title: "Issue Process"
description:
    "The process for documenting problems and projects. Issues are focused discussions when no vote is yet required."
layout: default
---

# Issue Process

The process for documenting problems and projects. Issues are focused discussions when no vote is yet required.

## What are Issues for?

Issues stored within [the FPA GIT repository](https://github.com/FreeCAD/FPA) represent different things:

- **Tasks that need to be done**: by an FPA admin, FPA member, or just anybody from the FreeCAD community. Anyone is free to open new issues they feel the FPA should work on or solve, or comment on open issues.
- **Problems that need to be discussed** at the FPA level **only**. FreeCAD-specific problems should be discussed in the FreeCAD repository.
- **Payments that need to be done**, once or recurring. All payments are identified with the **Payment** tag. Recurring payments, that have a term (ex. 05 installments) or no term (ex: one payment per month), also have the **Recurring payment** tag. Payments that need to be done monthly also have the **Monthly** tag. Finally, payments of grants have the **Grant** tag, while payments of contracts have the **Contract** tag.
- **Payments already done** receive the **Payment processed** tag once all the payments needed for that issue (once if only one payment, or ex. after the fifth installment for payments in 5 installments). The tag is added by the person paying the last installment. The issue is then closed by the FPA financial manager.

The tagging system is used to classify issues, it is specially important to use them for payment-related issues. All payments done, no matter the payment platform (bank transfer, paypal...) should **always indicate "FPA issue" + the FPA issue number** so it is easy to find and parse automatically. No payment should ever be made without an existing issue open.

It is important that each payment can always be repated to an issue. Issues history should be kept forever.

## Backing up

Issues are backed up in the `encrypted/issues-backup` folder, using the [ghbackup script](https://github.com/FreeCAD/issues-backup/blob/main/ghbackup.py) used for the FreeCAD issues. Usage:

```bash
cd encrypted/issues-backup
/path/to/ghbackup.py --all FreeCAD/FPA
git add .
git ci
git push
```

Backup is currently done manually once a week by the FPA chair.
