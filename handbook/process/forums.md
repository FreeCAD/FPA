---
title: "Forums Maintenance"
description:
    "The processes for handling maintenance of the FreeCAD Forums."
layout: default
---

# {{page.title}}

{{page.description}}

## Overview

The FreeCAD Forums are maintained by the FreeCAD Project Association, which pays their hosting costs, and is responsible for their general upkeep. This includes ensuring timely software updates, providing for server maintenance, and providing support to the Forums moderation team, including adding and removing members from that team as needed.

## General Server Software Maintenance

FreeCAD is hosted on two servers, fra1.freecad.io (matterbridge, wiki, old tracker) and fra2.freecad.io (main website and forums). Each of these servers hosts a series of linux lxd containers running Debian Buster, each container responsible for a single service, with an nginx reverse proxy providing external access to the appropriate subdomain. The primary point of contact for server maintenance is Kurt Kremitzki, with alternate contacts Yorik van Havre and Chris Hennes.

## Forum Administration

The FreeCAD Forum is hosted on fra2.freecad.io in an lxd container called "forum". This container hosts an instance of phpbb, the software that provides the Forum. Most maintenance of the forum is done via a web interface, but phpbb software updates are applied directly on the server.

### Adding a Moderator

(Technical steps here)

### Other Forums Maintenance Tasks

(Tasks here)
