import os 
import mne 
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.backends.backend_qt5agg
matplotlib.use('Qt5Agg')
mne.set_config('MNE_BROWSER_BACKEND', 'qt')

#change to load different recordings
directory = '/home/melissa/preprocessing/GRIN2B/GRIN2B_numpy'
os.chdir(directory)
data = np.load('227_GRIN2B.npy')
start_time = int(75128*240.4)
end_time = int(85128*250.4)
data = data[0:16, start_time:end_time]

os.chdir('/home/melissa/SleepScorer/')
montage_name = 'standard_16grid_taini1.elc'
montage = mne.channels.read_custom_montage(montage_name)
sample_rate = 250.4
channel_types=['eeg', 'emg', 'eeg', 'eeg', 'eeg', 'eeg', 'eeg', 'eeg',
                    'eeg', 'eeg', 'eeg', 'eeg', 'eeg', 'eeg', 'emg', 'eeg']

color_dict = dict(mag='darkblue', grad='b', eeg='k', eog='k', ecg='m',
     emg='g', ref_meg='steelblue', misc='k', stim='k',
     resp='k', chpi='k')

ch_names = ['S1Tr_RIGHT', 'EMG_RIGHT', 'M2_FrA_RIGHT', 'M2_ant_RIGHT', 'M1_ant_RIGHT', 'V2ML_RIGHT', 'V1M_RIGHT', 'S1HL_S1FL_RIGHT', 
           'V1M_LEFT', 'V2ML_LEFT', 'S1HL_S1FL_LEFT', 'M1_ant_LEFT', 'M2_ant_LEFT', 'M2_FrA_LEFT', 'EMG_LEFT', 'S1Tr_LEFT']

ch_numbers = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
info = mne.create_info(ch_names = ch_names, sfreq=sample_rate, ch_types=channel_types)

'This makes the object that contains all the data and info about the channels.'
'Computations like plotting, averaging, power spectrums can be performed on this object'

custom_raw = mne.io.RawArray(data, info, first_samp=5000)
custom_raw.plot(scalings = 'auto', color = color_dict, block=True) 
#duration = 10000, start = 5000, n_channels = 16)
