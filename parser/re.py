from matplotlib import pyplot as plt
import pandas as pd

class grideye():
  """Object to parse and plot grideye data."""
  def __init__(self, fn: str):
    self.fn = fn  
  
    def metadata():
      """
      Returns a dictionary with metadata for the columns in the grideye data.
      """
      description = {
        'Bubble': "*?* refers to location of measurement device", 
        'Node': "*?* refers to location of measurement device", 
        'Attribute': "*?* refers to location/type? of measurement device", 
        'Data time': "here comes a description", 
        'Voltage L1 min [V]': "Line to Neutral",
        'Voltage L1 avg [V]': "Line to Neutral", 
        'Voltage L1 max [V]': "Line to Neutral", 
        'Voltage L2 min [V]': "Line to Neutral",
        'Voltage L2 avg [V]': "Line to Neutral", 
        'Voltage L2 max [V]': "Line to Neutral", 
        'Voltage L3 min [V]': "Line to Neutral",
        'Voltage L3 avg [V]': "Line to Neutral", 
        'Voltage L3 max [V]': "Line to Neutral", 
        'Frequency L1 min [Hz]': "Grid voltage frequency",
        'Frequency L1 avg [Hz]': "Grid voltage frequency", 
        'Frequency L1 max [Hz]': "Grid voltage frequency",
        'Frequency L2 min [Hz]': "Grid voltage frequency", 
        'Frequency L2 avg [Hz]': "Grid voltage frequency",
        'Frequency L2 max [Hz]': "Grid voltage frequency", 
        'Frequency L3 min [Hz]': "Grid voltage frequency",
        'Frequency L3 avg [Hz]': "Grid voltage frequency", 
        'Frequency L3 max [Hz]': "Grid voltage frequency", 
        'THDS L1 max [%]': "Total Harmonic Distortion *s?* ",
        'THDS L2 max [%]': "Total Harmonic Distortion *s?* ", 
        'THDS L3 max [%]': "Total Harmonic Distortion *s?* ", 
        'Inverted Component [%]': "Sequence componets *?*",
        'Homopolar Component [%]': "Sequence componets *?*", 
        'Harmonics L1 max [%]': "Currrent harmonics",
        'Harmonics L2 max [%]': "Currrent harmonics", 
        'Harmonics L3 max [%]': "Currrent harmonics", 
        'Current L1 avg [A]': "Line currents *?*",
        'Current L1 max [A]': "Line currents *?*", 
        'Current L2 avg [A]': "Line currents *?*", 
        'Current L2 max [A]': "Line currents *?*",
        'Current L3 avg [A]': "Line currents *?*", 
        'Current L3 max [A]': "Line currents *?*", 
        'Current LN avg [A]': "Line currents *?*",
        'Current LN max [A]': "Line currents *?*", 
        'EPC L1 [kWh]': "*?* some kind of energy performance indicator", 
        'EPC L2 [kWh]': "*?* some kind of energy performance indicator", 
        'EPC L3 [kWh]': "*?* some kind of energy performance indicator",
        'EPP L1 [kWh]': "here comes a description", 
        'EPP L2 [kWh]': "here comes a description", 
        'EPP L3 [kWh]': "here comes a description",  
        'EQC L1 [kVarh]': "here comes a description",
        'EQC L2 [kVarh]': "here comes a description", 
        'EQC L3 [kVarh]': "here comes a description", 
        'EQP L1 [kVarh]': "here comes a description", 
        'EQP L2 [kVarh]': "here comes a description",
        'EQP L3 [kVarh]': "here comes a description", 
        'P L1 [kW]': "Power per-phase", 
        'P L2 [kW]': "Power per-phase", 
        'P L3 [kW]': "Power per-phase", 
        'Q L1 [kVar]': "Reactive power per-phase",
        'Q L2 [kVar]': "Reactive power per-phase", 
        'Q L3 [kVar]': "Reactive power per-phase", 
        'S L1 [kVA]': "Apparent power per-phase", 
        'S L2 [kVA]': "Apparent power per-phase", 
        'S L3 [kVA]': "Apparent power per-phase",
        'Cos phi L1': "Power factor", 
        'Cos phi L2': "Power factor", 
        'Cos phi L3': "Power factor", 
        'Unnamed: 62': "*?*"
        }
      return description

    self.metadata = metadata
