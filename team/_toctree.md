---
orphan: true
---

% This section has a mixture of links to external profiles
% and inline profiles that are pages on this site. If the
% inline profiles are included in the toctree, the sidebar
% is patchy, missing anyone who linked an external profile;
% meanwhile its sections duplicate those of the README.
%
% Instead of a toctree just use README as the master list.
%
% This file is here to suppress
% >  WARNING: document isn't included in any toctre
% for those inline profiles we do have.
%
% It works by making an orphan toctree, so all files in it
% are implicitly acknowledged as orphaned.

```{toctree}
:glob:
*/*
```
