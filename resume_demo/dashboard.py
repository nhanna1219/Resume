# Tùy chỉnh addmin-tools-stats
from admin_tools_stats.modules import DashboardCharts, get_active_graph

# append an app list module
self.children.append(modules.AppList(
    _('Dashboard Stats Settings'),
    models=('admin_tools_stats.*', ),
))

# Copy following code into your custom dashboard
# append following code after recent actions module or
# a link list module for "quick links"
graph_list = get_active_graph()
for i in graph_list:
    kwargs = {}
    kwargs['require_chart_jscss'] = True
    kwargs['graph_key'] = i.graph_key

    for key in context['request'].POST:
        if key.startswith('select_box_'):
            kwargs[key] = context['request'].POST[key]

    self.children.append(DashboardCharts(**kwargs))
