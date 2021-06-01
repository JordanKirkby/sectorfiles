# XA Sectorfiles Repository  

Sectorfiles for each FIR/ARTCC are stored and managed separately. This repository stores files using the same directory structure as Aurora. Sectorfile definitions (the `.isc` files) are stored in the root of the repository, and the referenced files are stored in `Include/XA/<name of FIR/ARTCC>/`. To contribute, fork this repository, make a new branch with a name following this pattern `<center>-<change>-<VID>` where `<center>` is a four letter ICAO code (e.g. `kzla`, `kzma`, `czyz`, etc.), `<change>` is what you wish to add/remove/update (e.g. `sid`, `star`, `airac`, etc. Consult the labels for ideas), and `<VID>` is your 6-digit IVAO VID. After reviewing the changes, the pull request will either be approved and merged (meaning the changes will appear in the next public release of the sector file), have modifications requested (typically as comments on the pull request), or will be rejected (the changes are not consistent in principle with the usage of our sectorfiles).  

## Getting Started  

To get started, press the "Fork" button on the top right of the [repository's main page](https://github.com/ivao-xa/sectorfiles). When you are done making changes, file a new [pull request](https://github.com/ivao-xa/sectorfiles/pulls), assign yourself, add the appropriate labels (described below), and request a reviewer. Thank you for your interest in contributing your time and efforts to our division.  

### Labels  

The following labels are currently in use for pull requests and issues:  
| label				| description
| -----				|-----------
| USA				| The addition/change is for an American ARTCC.
| Canada			| The addition/change is for a Canadian FIR.
| Bahamas			| The addition/change is for a Bahamian FIR.
| navigation		| The modification is of navigation data such as SIDs, STARs, fixes, VORs, airport information, airways, or holds.
| graphics			| The modification is of graphical data such as taxiway/runway/building labels, airport tfl files, or default colorschemes.
| bug				| This issue reports (or pull request addresses) an error or inconsistency in the previous version. This should not be used for updating out-of-date information.
| enhancement		| This adds a new feature or information significant enough to noticeably improve the quality of the sector file such as drawing a new major airport or adding procedures for an entire class of airports.
| duplicate			| This issue or pull request is similar enough to an existing one to not be considered as a separate item.
| documentation		| The modification only affects documentation such as the README or comments in the files. End users will notice no difference. Restructuring pre-existing data is also a valid use of this label.
| invalid			| Something is a bit 'off'. This is either not relevant, not reasonable, or in violation of a rule, regulation, policy, or norm of either IVAO HQ or the XA division.
| beginner friendly	| This issue or pull request is suitable for people with little prior experience.
| help wanted		| Information beyond what the current assignees possess is required to resolve the issue or pull request. Individuals with sufficient know-how are encouraged to contribute their expertise.

## More information  

Learn more about editing sectorfiles: <https://wiki.ivao.aero/en/home/devops/manuals/SectorFile_Definition>  

