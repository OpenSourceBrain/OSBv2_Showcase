import eden_simulator
import sys
from pyneuroml import pynml

filename = sys.argv[1] if len(sys.argv) > 1 else "../NeuroML2/ACnet2/LEMS_TwoCell.xml"
print(
    "Running a simulation of %s in EDEN v%s"
    % (
        filename,
        eden_simulator.__version__ if hasattr(eden_simulator, "__version__") else "???",
    )
)

results = eden_simulator.runEden(filename)

print("Completed simulation in EDEN, saved results: %s"%(results.keys()))

pyr_v = results['pyramidals/0/pyr_4_sym/0/v']
bask_v = results['baskets/0/bask/0/v']
times = results['t']

ax = pynml.generate_plot(
    [times, times],  # Add 2 sets of x values
    [pyr_v, bask_v],  # Add 2 sets of y values
    "Data from simulation in EDEN of %s"%filename,  # Title
    labels=['Pyr 0 soma','Bask 0 soma'],
    legend_position = "right",
    xaxis="Time (s)",  # x axis legend
    yaxis="Membrane potential (V)",  # y axis legend
    show_plot_already=False,  # Show or wait for plt.show()?
    font_size=10,  # Font
    title_above_plot = True,
    save_figure_to="eden_example.png",
)  # Save figure
