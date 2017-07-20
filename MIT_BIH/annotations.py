BEAT_ANNOTATION = {  # Same total as MIT BIH Arrhythmia Dataset
    '·': 'Normal beat', 
    'N': 'Normal beat', 
    'L': 'Left bundle branch block beat', 
    'R': 'Right bundle branch block beat', 
    'A': 'Atrial premature beat (APC, atrial premature complexes)',
    'a': 'Aberrated atrial premature beat',
    'J': 'Nodal (junctional) premature beat',
    'S': 'Supraventricular premature or ectopic beat (atrial or nodal)',
    'V': 'Premature ventricular contraction', 
    'F': 'Fusion of ventricular and normal beat',
    # '[': 'Start of ventricular flutter/fibrillation',  #
    '!': 'Ventricular flutter wave',  #
    # ']': 'End of ventricular flutter/fibrillation',  #
    'e': 'Atrial escape beat',
    'j': 'Nodal (junctional) escape beat',
    'E': 'Ventricular escape beat',
    '/': 'Paced beat',
    'f': 'Fusion of paced and normal beat',
    'x': 'Non-conducted P-wave (blocked APB)',  #
    'Q': 'Unclassifiable beat',
    # '|': 'Isolated QRS-like artifact'    
}

BEAT_ANNOTATION2 = {  # Same annot as MIT BIH Arrhythmia Dataset
    '·': 'Normal beat', 
    'N': 'Normal beat', 
    'L': 'Left bundle branch block beat', 
    'R': 'Right bundle branch block beat', 
    'A': 'Atrial premature beat (APC, atrial premature complexes)',
    'a': 'Aberrated atrial premature beat',
    'J': 'Nodal (junctional) premature beat',
    'S': 'Supraventricular premature or ectopic beat (atrial or nodal)',
    'V': 'Premature ventricular contraction', 
    'F': 'Fusion of ventricular and normal beat',
    '[': 'Start of ventricular flutter/fibrillation',  #
    '!': 'Ventricular flutter wave',  #
    ']': 'End of ventricular flutter/fibrillation',  #
    'e': 'Atrial escape beat',
    'j': 'Nodal (junctional) escape beat',
    'E': 'Ventricular escape beat',
    '/': 'Paced beat',
    'f': 'Fusion of paced and normal beat',
    'x': 'Non-conducted P-wave (blocked APB)',  #
    'Q': 'Unclassifiable beat',
    '|': 'Isolated QRS-like artifact'    
}

BEAT_ANNOTATION3 = {  # Same as MIT BIH all https://www.physionet.org/physiobank/annotations.shtml
    'N': 'Normal beat (displayed as "·" by the PhysioBank ATM, LightWAVE, pschart, and psfd)',
    'L': 'Left bundle branch block beat',
    'R': 'Right bundle branch block beat',
    'B': 'Bundle branch block beat (unspecified)',
    'A': 'Atrial premature beat',
    'a': 'Aberrated atrial premature beat',
    'J': 'Nodal (junctional) premature beat',
    'S': 'Supraventricular premature or ectopic beat (atrial or nodal)',
    'V': 'Premature ventricular contraction',
    'r': 'R-on-T premature ventricular contraction',
    'F': 'Fusion of ventricular and normal beat',
    'e': 'Atrial escape beat',
    'j': 'Nodal (junctional) escape beat',
    'n': 'Supraventricular escape beat (atrial or nodal)',
    'E': 'Ventricular escape beat',
    '/': 'Paced beat',
    'f': 'Fusion of paced and normal beat',
    'Q': 'Unclassifiable beat',
    '?': 'Beat not classified during learning'
}

BEAT_ANNOTATION4 = {  # Same annot as Proble paper M.G Tsipo
    # NORMAL
    '·': 'Normal beat', 
    'N': 'Normal beat', 
    '/': 'Paced beat',
    'f': 'Fusion of paced and normal beat',
    'x': 'Non-conducted P-wave (blocked APB)',  #
    'L': 'Left bundle branch block beat', 
    'R': 'Right bundle branch block beat', 
    'Q': 'Unclassifiable beat',
    # PVC
    'V': 'Premature ventricular contraction', 
    # VF
    '[': 'Start of ventricular flutter/fibrillation',
    '!': 'Ventricular flutter wave',
    ']': 'End of ventricular flutter/fibrillation',
    # Block
    '(BII': '2° heart block',
}

NON_BEAT_ANNOTATION = {
    '[': 'Start of ventricular flutter/fibrillation',
    '!': 'Ventricular flutter wave',
    ']': 'End of ventricular flutter/fibrillation',
    'x': 'Non-conducted P-wave (blocked APC)',
    '(': 'Waveform onset',
    ')': 'Waveform end',
    'p': 'Peak of P-wave',
    't': 'Peak of T-wave',
    'u': 'Peak of U-wave',
    '`': 'PQ junction',
    '\'': 'J-point',
    '^': '(Non-captured) pacemaker artifact',
    '|': 'Isolated QRS-like artifact [1]',
    '~': 'Change in signal quality [1]',
    '+': 'Rhythm change [2]',
    's': 'ST segment change [2]',
    'T': 'T-wave change [2]',
    '*': 'Systole',
    'D': 'Diastole',
    '=': 'Measurement annotation [2]',
    '"': 'Comment annotation [2]',
    '@': 'Link to external data [3]'
}

RHYTHM_ANNOTATION = {
    '(AB': 'Atrial bigeminy',
    '(AFIB': 'Atrial fibrillation',
    '(AFL': 'Atrial flutter',
    '(B': 'Ventricular bigeminy',
    '(BII': '2° heart block',
    '(IVR': 'Idioventricular rhythm',
    '(N': 'Normal sinus rhythm',
    '(NOD': 'Nodal (A-V junctional) rhythm',
    '(P': 'Paced rhythm',
    '(PREX': 'Pre-excitation (WPW)',
    '(SBR': 'Sinus bradycardia',
    '(SVTA': 'Supraventricular tachyarrhythmia',
    '(T': 'Ventricular trigeminy',
    '(VFL': 'Ventricular flutter',
    '(VT': 'Ventricular tachycardia',
}
