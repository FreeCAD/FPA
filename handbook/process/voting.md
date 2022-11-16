---
title: "Voting"
description:
    "How the FPA conducts a vote"
layout: default
---

# {{page.title}}

{{page.description}}

The voting process is designed to achieve three purposes:

1. To Concisely and formally describe what is being proposed
2. To facilitate discussion around the proposal
3. To allow members to formally offer their opinion in the form of a cast vote

This process is challenging because of the asynchronous functioning of the FPA. 
Not all members are available at the same time to take a voice poll.

In general, all votes follow the same pattern:

# Creating the Vote

Any member of the FPA may propose a vote.  This is done in the form of a forum
post to the [FreeCAD Project Association](https://forum.freecadweb.org/viewforum.php?f=43) subsection of the forum.

Vote topics MUST have the following:

* A title that matches the format:
    [Vote Required] <Summary of the Proposal>
* Be marked 'sticky' by opening the topic, using the tool in the
    'Mod' menu to "change to Sticky"
* The first post should describe the background and exactly what is being proposed.
* The first post should have a poll.
    * The poll should offer clear, non-overlapping options for votes.
    * The poll MUST include the option to 'Abstain' for anyone who doesn't feel qualified to offer an opinion.
    * The poll should be set to run 'indefinitely'
    * The poll should allow participants to change their vote. (allow re-voting)
    * Hide votes is turned off
    * Limit votes is turned off
    * Show poll voters is turned on
    * Show results ordered is turned off

# Addressing Comments and Feedback

The poll will run until it is either approved, defeated, or retracted by the submitter.

Replies to the topic will allow FPA members to offer feedback, ask questions, and
suggest improvements.

The submitter should moderate the topic.  Suggestions that are adopted should be reflected by editing the first post

People who have voted, MAY change their vote based on updates to the first post description. e.g. someone votes 'no' initially but changes the vote later because the objectionable elements have been changed.

If the text of the first post is changed, the vote MUST NOT be closed for at least 7 days to give people time to re-vote.


# Does the vote pass or fail?

There are two criteria that must be met for a vote to pass:
* At least half of the current active members must cast a vote (including voting to abstain)
* A majority of the votes cast must go to one of the options.

## Example
The vote is to do one of three things.  (9 active members, 8 voting)
Options are:
   thing 1 receives 2
   thing 2 receives 2
   thing 3 receives 0
   abstain gets 1 vote

   Result: voting continues


If a vote has options that are incremental, the vote will pass at the lowest common value that achieves success.

## Example
The vote is to spend an amount of money.  (9 active members, 8 voting)
Options are:
   $10 which receives 2 votes
   $20 which receives 4 votes
   $30 which receives 2 votes
   abstain gets 0 votes

This would pass at $20 because the people voting $20 and $30 are a majority and agree on at least $20.



# Closing the Vote

When the vote has either achieved consensus and passed or been defeated, the person who submitted it, or an admin member SHOULD close the vote.

* Edit the first post and change the poll.  Set the Run Poll to  'Until' and set the end time a minute or two in the future.  Then submit.  Within a minute the poll will expire and the votes will be locked.
* Remove the 'Sticky' from the topic.
* Update the [Decisions](../process/decisions) file
* If the vote added, removed, or otherwise changed FPA membership, update the [roster](../people/roster)
* Reply to the topic explaining the outcome.  (eg.  "This vote is passed by consensus"). This last post indicates when the initiative has passed and becomes effective unless the initiative itself contained an effective date.
