# Maintain the source that owns the skill

Use this reference for bundled or vendor-managed targets and material source/cache, pin, installation, or hook questions. Inspection remains read-only unless the task grants changes.

## Identify ownership and the durable target

Distinguish the standalone source, plugin repository, package manifest, generated cache, and installed copy. Verify only identities needed to avoid changing the wrong source or making an ephemeral repair. A writable installed directory does not prove it is the maintainable source.

For a user-maintained standalone skill, edit its confirmed source and update the installed copy only when installation is included in the grant. For a user-owned plugin, make changes in the plugin source, preserve unrelated components and metadata, and use its supported packaging and reinstall path when authorized. In a Codex environment, an available `plugin-creator` helper may supply existing-plugin guidance; otherwise consult the host's native tools and documentation. Do not scaffold a replacement plugin or add a marketplace merely because a quickstart offers that flow.

For a vendor-managed target, do not silently patch a generated cache or assume control of upstream source. A review can identify defects and supported options. Carry out a maintained wrapper, disablement, update, or exception only when that exact approach is authorized and compatible with controlling policy. If no supported writable source is established, report what remains blocked and continue independent review.

## Preserve pins and invocation policy

Read applicable owner policy and the relevant source/version state before proposing updates. Respect pinned branches, revisions, versions, and named exceptions. Do not fetch, merge, update, or reinstall a pinned dependency automatically. A modernization request does not cancel an explicit restriction; resolve an actual conflict before that action.

Before an authorized install or enablement, verify that resulting discovery and invocation settings match the owner's choice and the target host's actual policy. Metadata may be optional. On hosts using `allow_implicit_invocation`, accept supported Boolean `true`, Boolean `false`, or omission as applicable; reject malformed values or a result that contradicts a required setting. Preserve unrelated UI and dependency fields. Do not regenerate an entire metadata file just to change one field if that could erase policy. If setup or packaging changes an intended setting, resolve that mismatch within the grant before claiming successful delivery.

Treat skill discovery and hook execution as separate mechanisms. An explicit-only discovery setting does not disable plugin hooks or prove they cannot inject context. Inspect relevant hooks and their real configuration when they affect the review. Preserve the owner's hook policy, and do not add, enable, disable, or reconfigure hooks during an unrelated skill update. A declared hook does not establish runtime execution.

## Verify the authorized delivery

Qualify the native update path for the exact plugin and installation source. Editing a skill does not automatically authorize marketplace changes, publication, upstream submission, broader dependency upgrades, or changes to other bundled skills. A single explicit grant may include the necessary source edit, package validation, and reinstall; do not split it into additional approval stages.

After the authorized operation, read back the installed version or revision, affected skill content, invocation policy, and any material manifest or hook state. Distinguish source changes, packaged results, installed content, and actual application pickup. Reconcile a partial or unknown install before another mutation, and report any remaining mismatch without inventing success.
