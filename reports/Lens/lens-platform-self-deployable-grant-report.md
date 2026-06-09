# [Lens] Make Lens Platform Self-Deployable and Cloud-Agnostic #29 - Work Completed

## Project Overview
This project aimed to transform the Lens platform from an AWS-dependent system to a fully self-deployable, cloud-agnostic solution. The original proposal can be found at: [FPA Grant Proposal #29](https://github.com/FreeCAD/FPA-grant-proposals/issues/29)

**Goals Achieved:**
- Eliminated all AWS service dependencies (S3, Lambda)
- Created container orchestration with Docker Compose
- Implemented local storage and processing solutions
- Enabled self-hosting on any infrastructure
- Streamlined deployment process
- Documented code, service details, and workflows

## Pull Requests Summary

### Ondsel-Server Repository

- **[PR #1](https://github.com/FreeCAD/Ondsel-Server/pull/1)** - Revert company closing commits
  - Restored platform functionality after company closure

- **[PR #2](https://github.com/FreeCAD/Ondsel-Server/pull/2)** - Feature: Allow to use local storage instead of AWS S3
  - Replaced AWS S3 dependency with local file storage system
  - Added configurable storage backend option

- **[PR #3](https://github.com/FreeCAD/Ondsel-Server/pull/3)** - Add Docker Compose setup for local development
  - Implemented comprehensive Docker Compose configuration
  - Added services for frontend, backend, MongoDB, Matomo, and FC-Worker
  - Created default user migration scripts

- **[PR #4](https://github.com/FreeCAD/Ondsel-Server/pull/4)** - Integrated FreeCAD Celery Worker in docker-compose
  - Added FC-Worker API, Celery and Redis services to docker-compose

- **[PR #5](https://github.com/FreeCAD/Ondsel-Server/pull/5)** - Feature: Enable Hot Reloading for FC-Worker Code
  - Implemented hot-reloading for development workflow
  - Eliminated need to rebuild Docker containers for code changes

- **[PR #6](https://github.com/FreeCAD/Ondsel-Server/pull/6)** - Feature: Replace AWS-based Pre-signed URL Generation
  - Replaced AWS pre-signed URL generation with local implementation
  - Maintained security and access control

- **[PR #11](https://github.com/FreeCAD/Ondsel-Server/pull/11)** - Updated docs
  - Added comprehensive deployment and technical documentation
  - Documented service details and workflows
  - Included system requirements, installation steps, and configuration options

- **[PR #15](https://github.com/FreeCAD/Ondsel-Server/pull/15)** - Fixed bug initial model thumbnail
  - Resolved issues with initial model thumbnail display
  - Fixed .Brep format handling problems

- **[PR #16](https://github.com/FreeCAD/Ondsel-Server/pull/16)** - Feature: Added support to run LENS from prebuilds docker images
  - Added Docker Hub registry support for prebuilt images
  - Created docker-compose.prebuilds.yml configuration
  - Enabled easy deployment using prebuilt Docker images

### FC-Worker Repository

- **[PR #1](https://github.com/FreeCAD/FC-Worker/pull/1)** - Fixes apt source.list for updates
  - Temporary fix to enable Docker build process

- **[PR #2](https://github.com/FreeCAD/FC-Worker/pull/2)** - Feature: Implement Celery worker
  - Replaced AWS Lambda with Celery-based task queue system
  - Added Redis for message broker and result backend
  - Implemented parallel processing capabilities

- **[PR #3](https://github.com/FreeCAD/FC-Worker/pull/3)** - Feature: Add Development Environment for fc-worker
  - Enabled hot-reloading for FC-Worker development
  - Integrated with Ondsel-Server development workflow

## Total: 12 Pull Requests
- **Ondsel-Server:** 9 PRs
- **FC-Worker:** 3 PRs

**Status:** All tasks from the grant proposal completed successfully.
