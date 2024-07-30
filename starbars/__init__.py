"""
Visualize statistical significance on existing Matplotlib plots by adding
significance bars and p-value labels between chosen pairs of columns.
"""

import matplotlib.pyplot as plt

from .utils import pvalue_to_asterisks, get_positions

__version__ = "1.3.0"


def draw_annotation(annotations, ax=None, ns_show=True, bar_margin=0.03, tip_length=0.03,
                    fontsize=10, top_margin=0.03):
    """
    Draw statistical significance bars and p-value labels between chosen pairs of columns on existing plots.

    :param annotations: list of tuples containing the x-axis labels and the p-value of the pair.
    :type annotations: list[tuple[float | str, float | str, float]]
    :param ax: The axis of subplots to draw annotations on. If `ax` is not provided, it implies that you are working with a single plot rather than a set of subplots. In such cases, the annotations apply to the only existing plot in the figure.
    :type ax: matplotlib.axes.Axes
    :param ns_show: whether to show non-statistical bars. (Default: True)
    :param bar_margin: margin of the bar from data. Default is 3% of the data.
    :param tip_length: length of the tip of the statistical bar. Default is 3% relative to data range.
    :param fontsize: font size of the annotations.
    :param top_margin: margin of the last annotation from the top of the graph. Default is 3% of the data.
    """

    if ax is None:
        ax = plt.gca()

    y_min, y_max = ax.get_ylim()
    height = y_max

    # Get the positions of the values
    for (x1, x2, pvalue) in annotations:
        x1_position, x2_position = get_positions(ax, x1, x2)
        y1 = height + bar_margin * 0.8 * (height - y_min)
        h = tip_length * 0.8 * (height - y_min)
        text = pvalue_to_asterisks(pvalue)

        # Draw the statistical annotation
        if ns_show or text != 'ns':
            ax.plot([x1_position, x1_position, x2_position, x2_position], [y1, y1 + h, y1 + h, y1], lw=1.5, c="k")
            height = y1 + 2.5 * h
            ax.text((x1_position + x2_position) * .5, y1 + h + bar_margin, text, ha='center', va='bottom',
                    color="k", fontsize=fontsize)

        # Adjust the y-axis limit of the current subplot to accommodate the top margin
        y_min, y_max = ax.get_ylim()
        ax.set_ylim(y_min, y_max + top_margin * (height + y_max))