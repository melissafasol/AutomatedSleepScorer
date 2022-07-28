
import numpy as np
import mne
import os 


directory_path = '/home/melissa/preprocessing/GRIN2B/GRIN2B_numpy'
recording_file = np.load('137_GRIN2B.npy')



os.chdir('/home/melissa/preprocessing/numpyformat_baseline')
file = np.load('S7068_BASELINE.npy')

#plot original data file without specified time epochs 


montage_name = 'standard_16grid_taini1.elc'
montage = mne.channels.read_custom_montage(montage_name)
sample_rate = 250.4
channel_types=['eeg', 'eeg', 'eeg', 'eeg', 'eeg', 'eeg', 'eeg', 'eeg',
                    'eeg', 'eeg', 'eeg', 'eeg', 'eeg', 'eeg', 'emg', 'emg']

ch_names_1= ['S1Tr_RIGHT', 'EMG_RIGHT', 'M2_FrA_RIGHT', 'M2_ant_RIGHT', 'M1_ant_RIGHT', 'V2ML_RIGHT', 'V1M_RIGHT', 'S1HL_S1FL_RIGHT', 
           'V1M_LEFT', 'V2ML_LEFT', 'S1HL_S1FL_LEFT', 'M1_ant_LEFT', 'M2_ant_LEFT', 'M2_FrA_LEFT', 'EMG_LEFT', 'S1Tr_LEFT']

ch_names = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

#this creates the info that will go with the channels - names, sample rate and channel types
info = mne.create_info(ch_names =ch_names_1, sfreq=sample_rate, ch_types=channel_types)
custom_raw = mne.io.RawArray(recording_file, info)