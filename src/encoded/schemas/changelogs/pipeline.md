## Changelog for pipeline.json

### Schema version 6

* *aliases* now must be properly namespaced according lab.name:alphanumeric characters with no leading or trailing spaces
* unsafe characters such as " # @ % ^ & | ~ ; ` [ ] { } and consecutive whitespaces will no longer be allowed in the alias

### Schema version 5

* *assay_term_id* is no longer allowed to be submitted, it will be automatically calculated based on the term_name, if present

### Schema version 4

* array properties analysis_steps, aliases, documents and references must contain unique elements

### Schema version 3

* *version* field was removed
* *end_points* was removed
* *name* was removed

### Schema version 2

* *lab* field added
* *award* field added
