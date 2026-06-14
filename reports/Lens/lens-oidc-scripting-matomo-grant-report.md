# [LENS] OpenID Connect Authentication, FreeCAD Scripting in Viewer, and Matomo Docker Image Replacement #82 - Work Completed

## Project Overview
This project aimed to extend the Lens platform with enterprise-grade authentication, in-viewer FreeCAD scripting, and continued analytics support. The original proposal can be found at: [FPA Grant Proposal #82](https://github.com/FreeCAD/FPA-grant-proposals/issues/82)

**Goals Achieved:**
- Added OpenID Connect (OIDC) authentication for self-hosted identity providers like Keycloak
- Enabled users to run FreeCAD Python scripts and macros on models directly in the viewer
- Implemented a sandboxed code-execution runner in FC-Worker for safe script execution
- Replaced the no-longer-public Bitnami Matomo image with a maintained custom-built image
- Added comprehensive documentation for OIDC, scripting/macros, and Matomo migration

## Pull Requests Summary

### Ondsel-Server Repository

#### Matomo Docker Image Replacement
- **[PR #64](https://github.com/FreeCAD/Ondsel-Server/pull/64)** - Updated Matomo image
  - Replaced the no-longer-public `docker.io/bitnami/matomo:5` image with a maintained, custom-built Matomo image
  - Published the replacement image to Docker Hub: [amrit3701/bitnami-matomo](https://hub.docker.com/repository/docker/amrit3701/bitnami-matomo)
  - Preserved compatibility with the existing Matomo database schema and `matomo-db` (MariaDB)
  - Restored analytics functionality for deployments using the `matomo-enabled` profile

#### OpenID Connect (OIDC) Authentication
- **[PR #65](https://github.com/FreeCAD/Ondsel-Server/pull/65)** - feat(oauth): add OpenID Connect (OIDC) authentication support
  - Added a new userinfo-based `OidcStrategy` wired into Feathers OAuth, alongside the existing Google and GitHub OAuth (FPA Grant #60)
  - Resolves [Ondsel-Server Issue #62](https://github.com/FreeCAD/Ondsel-Server/issues/62)
  - Managed all OIDC configuration from the Xavier admin panel, applied at runtime with no env-vars and no restart required
  - Added a site-admin-only `POST /oidc-discovery` endpoint that reads `/.well-known/openid-configuration` to auto-fetch issuer endpoints in the admin UI
  - Implemented Just-In-Time user provisioning and email-based account linking between local users and OIDC identities
  - Added schema updates for `oauth.providers.oidc` on site-config and `oauthProviders.oidc.id` on users, with public site-config filtering to prevent client-secret exposure

#### FreeCAD Scripting and Macros in the Viewer
- **[PR #66](https://github.com/FreeCAD/Ondsel-Server/pull/66)** - Feature: Allow user execute python scripts
  - Added a JavaScript-based code editor for Python scripts integrated into the model viewer
  - Implemented object-annotation references (`<objLabel>`) to reference objects by label
  - Implemented selected-object references (`<selectedObject:N>`) for reusable macros that work across models
  - Resolved placeholders on the frontend before sending pre-resolved scripts and object mappings to the backend
  - Added on-hover preview showing the resolved Python code for each annotation
  - Displayed script output (stdout/stderr) in the frontend
  - Created a macros management page (list, add, edit, delete), distinguishing model-specific scripts from global macros
  - Added an admin interface to provide example macros visible to all users
  - Created a backend code-snippet service and run endpoint that queues tasks to FC-Worker

#### Documentation
- **[PR #70](https://github.com/FreeCAD/Ondsel-Server/pull/70)** - Added docs related to Macros
  - Documented the macros and in-viewer scripting feature
  - Added admin-panel documentation for setting up global macros
  - Provided usage guidance for object annotations and selected-object references

### FC-Worker Repository

#### Sandboxed Script Execution
- **[PR #10](https://github.com/FreeCAD/FC-Worker/pull/10)** - Feature: Add sandboxed FreeCAD Python snippet runner
  - Added a new `RUN_CODE_SNIPPET` command to the FC-Worker command dispatcher
  - Executed user-provided Python scripts against an opened FreeCAD document inside a restricted bubblewrap sandbox
  - Applied resource limits for CPU, memory, file size, processes, and open files
  - Used cgroup v2 `pids.max` to prevent fork bombs
  - Captured and safely truncated stdout/stderr to avoid deadlocks
  - Posted script output back as a runner-log entry with execution status
  - Aligned remaining Dockerfiles with the FreeCAD 1.0.2 base image

## Total: 5 Pull Requests
- **Ondsel-Server:** 4 PRs
- **FC-Worker:** 1 PR

## Key Achievements

### OpenID Connect Authentication
✅ OIDC authentication fully implemented and tested with Keycloak
✅ Just-In-Time user provisioning on first login
✅ Email-based account linking between local users and OIDC identities
✅ Runtime configuration via the Xavier admin panel — no restart required
✅ Issuer auto-discovery via `/.well-known/openid-configuration`
✅ Client secrets protected from exposure in the public API

### FreeCAD Scripting and Macros in the Viewer
✅ In-viewer Python code editor with syntax highlighting
✅ Object annotation (`<objLabel>`) and selected-object (`<selectedObject:N>`) references
✅ Frontend placeholder resolution with on-hover code preview
✅ Model-specific scripts and reusable global macros
✅ Admin-provided example macros visible to all users
✅ Script output (stdout/stderr) displayed in the frontend

### Sandboxed Execution (FC-Worker)
✅ New `RUN_CODE_SNIPPET` command for safe script execution
✅ Restricted bubblewrap sandbox preventing container escape
✅ CPU, memory, file-size, process, and open-file resource limits
✅ Fork-bomb protection via cgroup v2 `pids.max`
✅ Safe stdout/stderr capture with truncation

### Matomo Docker Image Replacement
✅ Replaced the no-longer-public Bitnami Matomo image with a maintained custom-built image
✅ Published replacement image to Docker Hub
✅ Preserved compatibility with the existing Matomo database and MariaDB
✅ Analytics restored for deployments using the `matomo-enabled` profile

### Documentation
✅ OIDC/Keycloak setup instructions
✅ Macros and in-viewer scripting documentation
✅ Global macros admin-panel guide
✅ Matomo migration notes

### Deployment
✅ Live LENS test instance deployed at http://34.206.70.141/ for community feedback

**Status:** All tasks from the grant proposal completed successfully.
