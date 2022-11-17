# # helper for gauge
# # this function takes in a difficulty, not an average
# def get_color_from_diff(diff):
#     if diff >= 60:
#         return 'red'
#     elif diff >= 30:
#         return 'gold'
#     else:
#         return 'green'
# #---
# gauge
def gauge_repl(matchobj, exam=False):
    global GAUGE_COUNT
    GAUGE_COUNT += 1
    avg_int = int(re.findall(AVG_REGEXP, matchobj[0])[0])
    diff_int = 100 - avg_int # difficulty = 100 - average score on problem; in the problem .md files, specify averages
    if exam:
        caption = f'The average score on this exam was {avg_int}%.'
        title = "Overall Difficulty"
    else:
        caption = f'The average score on this problem was {avg_int}%.'
        title = "Difficulty"
    diff_gauge = '''
<center><div id="myDiv<num>"></div></center>
<script type="text/javascript">
var data = [
{
    domain: { x: [0, 1], y: [0, 1] },
    value: <value>,
    title: { text: "<title>"},
    type: "indicator",
    mode: "gauge+number",
    gauge: {
        axis: {
            range: [0, 100]
        },
        bar: {
            color: "<color>"
        }
    }
}
];

var layout = { width: 300, 
            height: 200, 
            margin: { t: 0, b: 0 }, 
            font: {family: "-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Helvetica, Arial, sans-serif"},
            annotations: [{x: 0.5, y: 0.18, xref: 'paper', yref: 'paper', text: "<caption>", showarrow: false}]};
Plotly.newPlot('myDiv<num>', data, layout, {displayModeBar: false});
</script>
'''.replace('<value>', str(diff_int)) \
    .replace('<num>', str(GAUGE_COUNT)) \
    .replace('<color>', get_color_from_diff(int(diff_int))) \
    .replace('<caption>', caption) \
    .replace('<title>', title)

    return diff_gauge