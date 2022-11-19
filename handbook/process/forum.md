---
title: "Forum Maintenance"
description:
    "The processes for handling maintenance of the FreeCAD Forum."
layout: default
---

# {{page.title}}

{{page.description}}

## Overview

The FreeCAD Forum is maintained by the FreeCAD Project Association, which pays the hosting costs, and is responsible for its general upkeep. This includes ensuring timely software updates, providing for server maintenance, and providing support to the Forum moderation team, including adding and removing members from that team as needed.

## General Server Software Maintenance

FreeCAD is hosted on two servers, fra1.freecad.io (matterbridge, wiki, old tracker) and fra2.freecad.io (main website and forum). Each of these servers hosts a series of linux lxd containers running Debian Buster, each container responsible for a single service, with an nginx reverse proxy providing external access to the appropriate subdomain. The primary point of contact for server maintenance is Kurt Kremitzki, with alternate contacts Yorik van Havre and Chris Hennes.

## Forum Administration

The FreeCAD Forum is hosted on fra2.freecad.io in an lxd container called "forum". This container hosts an instance of phpbb, the software that provides the Forum. Most maintenance of the forum is done via a web interface, but phpbb software updates are applied directly on the server.

### Adding a Moderator

When asked to do so by the Forum moderation team, an FPA member with Administrator privileges on the FreeCAD Forum will add a registered forum user to the "Global moderators" group. To do so:
1) Log into the FreeCAD forum
2) Click the icon for accessing the administrative area
3) Re-authenticate
4) Choose "Manager users" from the left-hand sidebar
5) Enter the username to modify
6) Select "Global moderators" from the "Add user to group:" drop-down menu
7) Click "Submit"

Removing a moderator is a similar process: omit steps 6 and 7, and instead click "Remove member from group".

### Other Forums Maintenance Tasks

phpbb issues periodic software updates -- when needed, the primary server administrator (Kurt Kremitzki) applies these updates, along with any other server maintenance tasks.
