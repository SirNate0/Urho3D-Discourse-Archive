rku | 2017-01-02 01:11:38 UTC | #1

Could anyone provide example how to make ListView with collapsible children? Much like scene hierarchy view in editor. Tried looking for it in editor scripts myself but it is not exactly clearest code around so.. halp. =x

EDIT: For next poor soul that will read this thread:
[code]
    list->SetHierarchyMode(true);
    Text* el = new Text(context_);
    list->InsertItem(M_MAX_UNSIGNED, el);
    Text* el2 = new Text(context_);
    list->InsertItem(M_MAX_UNSIGNED, el2, el);
[/code]

-------------------------

