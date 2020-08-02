import cPickle, base64
try:
	from SimpleSession.versions.v65 import beginRestore,\
	    registerAfterModelsCB, reportRestoreError, checkVersion
except ImportError:
	from chimera import UserError
	raise UserError('Cannot open session that was saved in a'
	    ' newer version of Chimera; update your version')
checkVersion([1, 13, 41780])
import chimera
from chimera import replyobj
replyobj.status('Restoring session...', \
    blankAfter=0)
replyobj.status('Beginning session restore...', \
    blankAfter=0, secondary=True)
beginRestore()

def restoreCoreModels():
	from SimpleSession.versions.v65 import init, restoreViewer, \
	     restoreMolecules, restoreColors, restoreSurfaces, \
	     restoreVRML, restorePseudoBondGroups, restoreModelAssociations
	molInfo = cPickle.loads(base64.b64decode('gAJ9cQEoVRFyaWJib25JbnNpZGVDb2xvcnECSwZOfYdVCWJhbGxTY2FsZXEDSwZHP8mZmaAAAAB9h1UJcG9pbnRTaXplcQRLBkc/8AAAAAAAAH2HVQVjb2xvcnEFSwZLAH1xBihLAV1xB0sBYUsCXXEISwJhSwNdcQlLA2FLBF1xCksEYUsFXXELSwVhdYdVCnJpYmJvblR5cGVxDEsGSwB9h1UKc3RpY2tTY2FsZXENSwZHP+AAAAAAAAB9h1UMbW1DSUZIZWFkZXJzcQ5dcQ8oTk5OTk5OZVUMYXJvbWF0aWNNb2RlcRBLBksBfYdVCnZkd0RlbnNpdHlxEUsGR0AUAAAAAAAAfYdVBmhpZGRlbnESSwaJfYdVDWFyb21hdGljQ29sb3JxE0sGTn2HVQ9yaWJib25TbW9vdGhpbmdxFEsGSwB9h1UJYXV0b2NoYWlucRVLBoh9h1UKcGRiVmVyc2lvbnEWSwZLAH2HVQhvcHRpb25hbHEXfXEYVQhvcGVuZWRBc3EZiIlLBihVMS9Vc2Vycy90ZW1lbHNvYi9Eb3dubG9hZHMvY29vcmRzL1MyLUExLURNQTEtMS54eXpxGk5OSwF0cRt9cRwoKFUqL1VzZXJzL3RlbWVsc29iL0Rvd25sb2Fkcy9jb29yZHMvMy1JLWQueHl6cR1OTksBdHEeXXEfSwJhKFUrL1VzZXJzL3RlbWVsc29iL0Rvd25sb2Fkcy9jb29yZHMvQTFXMy0xLnh5enEgTk5LAXRxIV1xIksEYShVMS9Vc2Vycy90ZW1lbHNvYi9Eb3dubG9hZHMvY29vcmRzL3dhdGVyLTYtQkstMS54eXpxI05OSwF0cSRdcSVLAGEoVTovVXNlcnMvdGVtZWxzb2IvRG93bmxvYWRzL2Nvb3Jkcy9jb3JhbnV1bGVuZV93YXRlci1vdXQueHl6cSZOTksBdHEnXXEoSwVhKFUrL1VzZXJzL3RlbWVsc29iL0Rvd25sb2Fkcy9jb29yZHMvMV8yLUExLnh5enEpTk5LAXRxKl1xK0sBYXWHh3NVD2xvd2VyQ2FzZUNoYWluc3EsSwaJfYdVCWxpbmVXaWR0aHEtSwZHP/AAAAAAAAB9h1UPcmVzaWR1ZUxhYmVsUG9zcS5LBksAfYdVBG5hbWVxL0sGWEsAAABTMlczLUlfZCBFW1JJLU1QMi9hVltEVFFdWi8vTVAyLzYtMzErRypdIC0xNjI3LjAwMTMgLTEsNjI3LjkxNjEgLTEsNjI4LjIxNzZ9cTAoWAYAAAA2LUJLLTFdcTFLAGFYIAAAAEFjZW5hcGh0aGVuZS0oSDJPKTMgSXNvbWVyIGVmcC0zXXEySwRhWDcAAAAxXzItQTEgRVtSSS1NUDIvYVZbRFRRXVpdCS04NTEuNjI3NAktODUyLjExMzUJLTg1Mi4yNzQ3XXEzSwFhWCEAAABwcmluY2lwYWwgbW9tZW50IGFsaWduZWQgZ2VvbWV0cnldcTRLBWFYSwAAAFMyLUExLURNQTFfRUZQLUQtMzAtcHc5MSAGBkVlPTAuMzEga2MvbSAGBkUwPTAuMjcga2MvbSAGBkcoMjk4Syk9IDAuMTkga2MvbV1xNUsDYXWHVQ9hcm9tYXRpY0Rpc3BsYXlxNksGiX2HVQ9yaWJib25TdGlmZm5lc3NxN0sGRz/pmZmZmZmafYdVCnBkYkhlYWRlcnNxOF1xOSh9cTp9cTt9cTx9cT19cT59cT9lVQNpZHNxQEsGSwBLAIZ9cUEoSwNLAIZdcUJLA2FLAksAhl1xQ0sCYUsFSwCGXXFESwVhSwFLAIZdcUVLAWFLBEsAhl1xRksEYXWHVQ5zdXJmYWNlT3BhY2l0eXFHSwZHv/AAAAAAAAB9h1UQYXJvbWF0aWNMaW5lVHlwZXFISwZLAn2HVRRyaWJib25IaWRlc01haW5jaGFpbnFJSwaIfYdVB2Rpc3BsYXlxSksGiH2HdS4='))
	resInfo = cPickle.loads(base64.b64decode('gAJ9cQEoVQZpbnNlcnRxAksGVQEgfYdVC2ZpbGxEaXNwbGF5cQNLBol9h1UEbmFtZXEESwZYAwAAAFVOS32HVQVjaGFpbnEFSwZYAQAAACB9h1UOcmliYm9uRHJhd01vZGVxBksGSwJ9h1UCc3NxB0sGiYmGfYdVCG1vbGVjdWxlcQhLBksAfXEJKEsBTl1xCksBSwGGcQthhksCTl1xDEsCSwGGcQ1hhksDTl1xDksDSwGGcQ9hhksETl1xEEsESwGGcRFhhksFTl1xEksFSwGGcRNhhnWHVQtyaWJib25Db2xvcnEUSwZOfYdVBWxhYmVscRVLBlgAAAAAfYdVCmxhYmVsQ29sb3JxFksGTn2HVQhmaWxsTW9kZXEXSwZLAX2HVQVpc0hldHEYSwaJfYdVC2xhYmVsT2Zmc2V0cRlLBk59h1UIcG9zaXRpb25xGl1xGyhLAUsBhnEcSwFLAYZxHUsBSwGGcR5LAUsBhnEfSwFLAYZxIEsBSwGGcSFlVQ1yaWJib25EaXNwbGF5cSJLBol9h1UIb3B0aW9uYWxxI31VBHNzSWRxJEsGSv////99h3Uu'))
	atomInfo = cPickle.loads(base64.b64decode('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'))
	bondInfo = cPickle.loads(base64.b64decode('gAJ9cQEoVQVjb2xvcnECS4NOfYdVBWF0b21zcQNdcQQoXXEFKEsMSw1lXXEGKEsMSw5lXXEHKEsPSxBlXXEIKEsPSxFlXXEJKEsSSxNlXXEKKEsSSxRlXXELKEsVSxZlXXEMKEsVSxdlXXENKEsYSxllXXEOKEsYSxplXXEPKEsbSxxlXXEQKEsbSx1lXXERKEseSx9lXXESKEseSyBlXXETKEseSyFlXXEUKEseSyJlXXEVKEshSyNlXXEWKEsiSyRlXXEXKEslSyZlXXEYKEslSydlXXEZKEsoSyllXXEaKEsoSyplXXEbKEsrSyxlXXEcKEsrSy1lXXEdKEsrSy5lXXEeKEsrSy9lXXEfKEssSzBlXXEgKEsuSzFlXXEhKEsySzNlXXEiKEsySzRlXXEjKEsySzVlXXEkKEsySzZlXXElKEszSzdlXXEmKEs1SzhlXXEnKEs5SzplXXEoKEs5SztlXXEpKEs8Sz1lXXEqKEs8Sz5lXXErKEs/S0BlXXEsKEs/S0FlXXEtKEtCS0NlXXEuKEtCS0RlXXEvKEtES0VlXXEwKEtES0ZlXXExKEtES0dlXXEyKEtIS0llXXEzKEtIS0plXXE0KEtKS0tlXXE1KEtKS0xlXXE2KEtKS01lXXE3KEtOS09lXXE4KEtOS1BlXXE5KEtOS1FlXXE6KEtOS1hlXXE7KEtPS1JlXXE8KEtPS1NlXXE9KEtPS1RlXXE+KEtQS1VlXXE/KEtQS1ZlXXFAKEtQS1dlXXFBKEtZS1plXXFCKEtZS1tlXXFDKEtZS1xlXXFEKEtZS11lXXFFKEteS19lXXFGKEteS2ZlXXFHKEteS2dlXXFIKEtfS2BlXXFJKEtfS2FlXXFKKEtgS2JlXXFLKEtgS3JlXXFMKEthS2NlXXFNKEthS3NlXXFOKEtiS2RlXXFPKEtiS3BlXXFQKEtjS2VlXXFRKEtjS3FlXXFSKEtkS2ZlXXFTKEtkS25lXXFUKEtlS2dlXXFVKEtlS29lXXFWKEtmS2hlXXFXKEtnS2llXXFYKEtoS2llXXFZKEtoS2plXXFaKEtoS2xlXXFbKEtpS2tlXXFcKEtpS21lXXFdKEt0S3VlXXFeKEt0S3ZlXXFfKEt3S3hlXXFgKEt3S3llXXFhKEt6S3tlXXFiKEt6S3xlXXFjKEt9S35lXXFkKEt9S4FlXXFlKEt9S4ZlXXFmKEt+S39lXXFnKEt+S4llXXFoKEt/S4BlXXFpKEt/S4JlXXFqKEuAS4FlXXFrKEuAS4VlXXFsKEuBS4plXXFtKEuCS4NlXXFuKEuCS5BlXXFvKEuDS4RlXXFwKEuDS5FlXXFxKEuES4VlXXFyKEuES5JlXXFzKEuFS4xlXXF0KEuGS4dlXXF1KEuGS45lXXF2KEuHS4hlXXF3KEuHS5NlXXF4KEuIS4llXXF5KEuIS5RlXXF6KEuJS49lXXF7KEuKS4tlXXF8KEuKS41lXXF9KEuLS4xlXXF+KEuLS5VlXXF/KEuMS5ZlXXGAKEuNS45lXXGBKEuNS5dlXXGCKEuOS5hlXXGDKEuPS5BlXXGEKEuPS5llXXGFKEuQS5plXXGGKEubS5xlXXGHKEubS51lZVUFbGFiZWxxiEuDWAAAAAB9h1UIaGFsZmJvbmRxiUuDiH2HVQZyYWRpdXNxikuDRz/JmZmgAAAAfYdVC2xhYmVsT2Zmc2V0cYtLg059h1UIZHJhd01vZGVxjEuDSwF9h1UIb3B0aW9uYWxxjX1VB2Rpc3BsYXlxjkuDSwJ9h3Uu'))
	crdInfo = cPickle.loads(base64.b64decode('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'))
	surfInfo = {'category': (6, u'main', {}), 'probeRadius': (6, 1.4, {}), 'pointSize': (6, 1, {}), 'name': [u'MSMS main surface of 6-BK-1', u'MSMS main surface of 1_2-A1 E[RI-MP2/aV[DTQ]Z]\t-851.6274\t-852.1135\t-852.2747', u'MSMS main surface of S2W3-I_d E[RI-MP2/aV[DTQ]Z//MP2/6-31+G*] -1627.0013 -1,627.9161 -1,628.2176', u'MSMS main surface of S2-A1-DMA1_EFP-D-30-pw91 \x06\x06Ee=0.31 kc/m \x06\x06E0=0.27 kc/m \x06\x06G(298K)= 0.19 kc/m', u'MSMS main surface of Acenaphthene-(H2O)3 Isomer efp-3', u'MSMS main surface of principal moment aligned geometry'], 'density': (6, 2, {}), 'colorMode': (6, 1, {}), 'useLighting': (6, True, {}), 'transparencyBlendMode': (6, 1, {}), 'molecule': [0, 1, 2, 3, 4, 5], 'smoothLines': (6, False, {}), 'lineWidth': (6, 1, {}), 'allComponents': (6, True, {}), 'twoSidedLighting': (6, True, {}), 'customVisibility': [None, None, None, None, None, None], 'drawMode': (6, 1, {}), 'display': (6, True, {}), 'customColors': [(0, None, {}), (0, None, {}), (0, None, {}), (0, None, {}), (0, None, {}), (0, None, {})]}
	vrmlInfo = {'subid': (0, None, {}), 'display': (0, None, {}), 'id': (0, None, {}), 'vrmlString': [], 'name': (0, None, {})}
	colors = {u'Ru': ((0.141176, 0.560784, 0.560784), 1, u'default'), u'Re': ((0.14902, 0.490196, 0.670588), 1, u'default'), u'Rf': ((0.8, 0, 0.34902), 1, u'default'), u'Ra': ((0, 0.490196, 0), 1, u'default'), u'Rb': ((0.439216, 0.180392, 0.690196), 1, u'default'), u'Rn': ((0.258824, 0.509804, 0.588235), 1, u'default'), u'Rh': ((0.0392157, 0.490196, 0.54902), 1, u'default'), u'Be': ((0.760784, 1, 0), 1, u'default'), u'Ba': ((0, 0.788235, 0), 1, u'default'), u'Bh': ((0.878431, 0, 0.219608), 1, u'default'), u'Bi': ((0.619608, 0.309804, 0.709804), 1, u'default'), u'Bk': ((0.541176, 0.309804, 0.890196), 1, u'default'), u'Br': ((0.65098, 0.160784, 0.160784), 1, u'default'), u'H': ((1, 1, 1), 1, u'default'), u'P': ((1, 0.501961, 0), 1, u'default'), u'Os': ((0.14902, 0.4, 0.588235), 1, u'default'), u'Es': ((0.701961, 0.121569, 0.831373), 1, u'default'), u'Hg': ((0.721569, 0.721569, 0.815686), 1, u'default'), u'Ge': ((0.4, 0.560784, 0.560784), 1, u'default'), u'Gd': ((0.270588, 1, 0.780392), 1, u'default'), u'Ga': ((0.760784, 0.560784, 0.560784), 1, u'default'), u'Pr': ((0.85098, 1, 0.780392), 1, u'default'),
u'Pt': ((0.815686, 0.815686, 0.878431), 1, u'default'), u'Pu': ((0, 0.419608, 1), 1, u'default'), u'C': ((0.564706, 0.564706, 0.564706), 1, u'default'), u'Pb': ((0.341176, 0.34902, 0.380392), 1, u'default'), u'Pa': ((0, 0.631373, 1), 1, u'default'), u'Pd': ((0, 0.411765, 0.521569), 1, u'default'), u'Xe': ((0.258824, 0.619608, 0.690196), 1, u'default'), u'Po': ((0.670588, 0.360784, 0), 1, u'default'), u'Pm': ((0.639216, 1, 0.780392), 1, u'default'), u'Hs': ((0.901961, 0, 0.180392), 1, u'default'), u'Ho': ((0, 1, 0.611765), 1, u'default'), u'Hf': ((0.301961, 0.760784, 1), 1, u'default'), u'Mo': ((0.329412, 0.709804, 0.709804), 1, u'default'), u'He': ((0.85098, 1, 1), 1, u'default'), u'Md': ((0.701961, 0.0509804, 0.65098), 1, u'default'), u'Mg': ((0.541176, 1, 0), 1, u'default'), u'K': ((0.560784, 0.25098, 0.831373), 1, u'default'), u'Mn': ((0.611765, 0.478431, 0.780392), 1, u'default'), u'O': ((1, 0.0509804, 0.0509804), 1, u'default'), u'Mt': ((0.921569, 0, 0.14902), 1, u'default'), u'S': ((1, 1, 0.188235), 1, u'default'), u'W': ((0.129412, 0.580392, 0.839216), 1, u'default'),
u'sky blue': ((0.529412, 0.807843, 0.921569), 1, u'default'), u'Zn': ((0.490196, 0.501961, 0.690196), 1, u'default'), u'plum': ((0.866667, 0.627451, 0.866667), 1, u'default'), u'Eu': ((0.380392, 1, 0.780392), 1, u'default'), u'Zr': ((0.580392, 0.878431, 0.878431), 1, u'default'), u'Er': ((0, 0.901961, 0.458824), 1, u'default'), u'Ni': ((0.313725, 0.815686, 0.313725), 1, u'default'), u'No': ((0.741176, 0.0509804, 0.529412), 1, u'default'), u'Na': ((0.670588, 0.360784, 0.94902), 1, u'default'), u'Nb': ((0.45098, 0.760784, 0.788235), 1, u'default'), u'Nd': ((0.780392, 1, 0.780392), 1, u'default'), u'Ne': ((0.701961, 0.890196, 0.960784), 1, u'default'), u'Np': ((0, 0.501961, 1), 1, u'default'), u'Fr': ((0.258824, 0, 0.4), 1, u'default'), u'Fe': ((0.878431, 0.4, 0.2), 1, u'default'), u'Fm': ((0.701961, 0.121569, 0.729412), 1, u'default'), u'B': ((1, 0.709804, 0.709804), 1, u'default'), u'F': ((0.564706, 0.878431, 0.313725), 1, u'default'), u'Sr': ((0, 1, 0), 1, u'default'), u'N': ((0.188235, 0.313725, 0.972549), 1, u'default'), u'Kr': ((0.360784, 0.721569, 0.819608), 1, u'default'),
u'Si': ((0.941176, 0.784314, 0.627451), 1, u'default'), u'Sn': ((0.4, 0.501961, 0.501961), 1, u'default'), u'Sm': ((0.560784, 1, 0.780392), 1, u'default'), u'V': ((0.65098, 0.65098, 0.670588), 1, u'default'), u'Sc': ((0.901961, 0.901961, 0.901961), 1, u'default'), u'Sb': ((0.619608, 0.388235, 0.709804), 1, u'default'), u'Sg': ((0.85098, 0, 0.270588), 1, u'default'), u'Se': ((1, 0.631373, 0), 1, u'default'), u'Co': ((0.941176, 0.564706, 0.627451), 1, u'default'), u'Cm': ((0.470588, 0.360784, 0.890196), 1, u'default'), u'Cl': ((0.121569, 0.941176, 0.121569), 1, u'default'), u'Ca': ((0.239216, 1, 0), 1, u'default'), u'Cf': ((0.631373, 0.211765, 0.831373), 1, u'default'), u'Ce': ((1, 1, 0.780392), 1, u'default'), u'Cd': ((1, 0.85098, 0.560784), 1, u'default'), u'Lu': ((0, 0.670588, 0.141176), 1, u'default'), u'light green': ((0.564706, 0.933333, 0.564706), 1, u'default'), u'Cs': ((0.341176, 0.0901961, 0.560784), 1, u'default'), u'Cr': ((0.541176, 0.6, 0.780392), 1, u'default'), u'Cu': ((0.784314, 0.501961, 0.2), 1, u'default'), u'La': ((0.439216, 0.831373, 1), 1, u'default'),
u'Li': ((0.8, 0.501961, 1), 1, u'default'), u'Tl': ((0.65098, 0.329412, 0.301961), 1, u'default'), u'Tm': ((0, 0.831373, 0.321569), 1, u'default'), u'Lr': ((0.780392, 0, 0.4), 1, u'default'), u'Th': ((0, 0.729412, 1), 1, u'default'), u'Ti': ((0.74902, 0.760784, 0.780392), 1, u'default'), u'tan': ((0.823529, 0.705882, 0.54902), 1, u'default'), u'Te': ((0.831373, 0.478431, 0), 1, u'default'), u'Tb': ((0.188235, 1, 0.780392), 1, u'default'), u'Tc': ((0.231373, 0.619608, 0.619608), 1, u'default'), u'Ta': ((0.301961, 0.65098, 1), 1, u'default'), u'Yb': ((0, 0.74902, 0.219608), 1, u'default'), u'Db': ((0.819608, 0, 0.309804), 1, u'default'), u'Dy': ((0.121569, 1, 0.780392), 1, u'default'), u'I': ((0.580392, 0, 0.580392), 1, u'default'), u'salmon': ((0.980392, 0.501961, 0.447059), 1, u'default'), u'U': ((0, 0.560784, 1), 1, u'default'), u'Y': ((0.580392, 1, 1), 1, u'default'), u'Ac': ((0.439216, 0.670588, 0.980392), 1, u'default'), u'Ag': ((0.752941, 0.752941, 0.752941), 1, u'default'), u'Ir': ((0.0901961, 0.329412, 0.529412), 1, u'default'), u'Am': ((0.329412, 0.360784, 0.94902), 1, u'default'),
u'Al': ((0.74902, 0.65098, 0.65098), 1, u'default'), u'As': ((0.741176, 0.501961, 0.890196), 1, u'default'), u'Ar': ((0.501961, 0.819608, 0.890196), 1, u'default'), u'Au': ((1, 0.819608, 0.137255), 1, u'default'), u'At': ((0.458824, 0.309804, 0.270588), 1, u'default'), u'In': ((0.65098, 0.458824, 0.45098), 1, u'default'), u'light gray': ((0.827451, 0.827451, 0.827451), 1, u'default')}
	materials = {u'default': ((0.85, 0.85, 0.85), 30)}
	pbInfo = {'category': [u'distance monitor', u'hydrogen bonds'], 'bondInfo': [{'color': (0, None, {}), 'atoms': [], 'label': (0, None, {}), 'halfbond': (0, None, {}), 'labelColor': (0, None, {}), 'labelOffset': (0, None, {}), 'drawMode': (0, None, {}), 'display': (0, None, {})}, {'color': (27, 13, {}), 'atoms': [[14, 15], [16, 18], [17, 27], [20, 21], [22, 27], [25, 12], [29, 24], [35, 37], [36, 40], [39, 31], [42, 32], [48, 53], [49, 52], [55, 57], [56, 60], [59, 47], [62, 63], [65, 54], [73, 70], [88, 77], [88, 75], [81, 71], [90, 75], [93, 69], [118, 119], [120, 122], [123, 116]], 'label': (27, u'', {}), 'halfbond': (27, False, {}), 'labelColor': (27, None, {}), 'labelOffset': (27, chimera.Vector(-1e+99, 0.0, 0.0), {chimera.Vector(-1e+99, 0.0, 0.0): [7], chimera.Vector(-1e+99, 0.0, 0.0): [21], chimera.Vector(-1e+99, 0.0, 0.0): [22], chimera.Vector(-1e+99, 0.0, 0.0): [23], chimera.Vector(-1e+99, 0.0, 0.0): [24], chimera.Vector(-1e+99, 0.0, 0.0): [2], chimera.Vector(-1e+99, 0.0, 0.0): [4], chimera.Vector(-1e+99, 0.0, 0.0): [26], chimera.Vector(-1e+99, 0.0, 0.0): [9], chimera.Vector(-1e+99, 0.0, 0.0): [1], chimera.Vector(-1e+99, 0.0, 0.0): [25], chimera.Vector(-1e+99, 0.0, 0.0): [13], chimera.Vector(-1e+99, 0.0, 0.0): [0], chimera.Vector(-1e+99, 0.0, 0.0): [10], chimera.Vector(-1e+99, 0.0, 0.0): [11], chimera.Vector(-1e+99, 0.0, 0.0): [12], chimera.Vector(-1e+99, 0.0, 0.0): [3], chimera.Vector(-1e+99, 0.0, 0.0): [14], chimera.Vector(-1e+99, 0.0, 0.0): [15], chimera.Vector(-1e+99, 0.0, 0.0): [16], chimera.Vector(-1e+99, 0.0, 0.0): [17], chimera.Vector(-1e+99, 0.0, 0.0): [18], chimera.Vector(-1e+99, 0.0, 0.0): [19], chimera.Vector(-1e+99, 0.0, 0.0): [6], chimera.Vector(-1e+99, 0.0, 0.0): [20], chimera.Vector(-1e+99, 0.0, 0.0): [8]}),
'drawMode': (27, 0, {}), 'display': (27, 2, {})}], 'lineType': (2, 1, {2: [0]}), 'color': (2, 11, {12: [1]}), 'optional': {'fixedLabels': (True, False, (2, False, {None: [1]}))}, 'display': (2, True, {}), 'showStubBonds': (2, False, {}), 'lineWidth': (2, 1, {}), 'stickScale': (2, 1, {}), 'id': [-2, -1]}
	modelAssociations = {}
	colorInfo = (16, (u'', (0, 0, 1, 1)), {(u'H', (1, 1, 1, 1)): [7], (u'S', (1, 1, 0.188235, 1)): [8], (u'light green', (0.564706, 0.933333, 0.564706, 1)): [3], (u'N', (0.188235, 0.313725, 0.972549, 1)): [9], (u'green', (0, 1, 0, 1)): [15], (u'O', (1, 0.0509804, 0.0509804, 1)): [6], (u'sky blue', (0.529412, 0.807843, 0.921569, 1)): [1], (u'tan', (0.823529, 0.705882, 0.54902, 1)): [0], (u'plum', (0.866667, 0.627451, 0.866667, 1)): [2], (u'light gray', (0.827451, 0.827451, 0.827451, 1)): [5], (u'salmon', (0.980392, 0.501961, 0.447059, 1)): [4], (u'white', (1, 1, 1, 1)): [14], (u'C', (0.564706, 0.564706, 0.564706, 1)): [10], (u'gray', (0.745, 0.745, 0.745, 1)): [12]})
	viewerInfo = {'cameraAttrs': {'center': (9.3963327286629, -5.2188747823001, -0.095359999999999), 'fieldOfView': 25.50160439021, 'nearFar': (16.239534862196, -16.430254862196), 'ortho': False, 'eyeSeparation': 50.8, 'focal': -0.095359999999999}, 'viewerAttrs': {'silhouetteColor': None, 'clipping': False, 'showSilhouette': True, 'showShadows': False, 'viewSize': 17.330834895913, 'labelsOnTop': True, 'depthCueRange': (0.5, 1), 'silhouetteWidth': 2, 'singleLayerTransparency': True, 'shadowTextureSize': 2048, 'backgroundImage': [None, 1, 2, 1, 0, 0], 'backgroundGradient': [(None, [(0.941176, 0.941176, 0.941176, 1), (0.741176, 0.741176, 0.741176, 1), (0.388235, 0.388235, 0.388235, 1)], 1), 1, 0, 0], 'depthCue': False, 'highlight': 0, 'scaleFactor': 1.2070993261352, 'angleDependentTransparency': True, 'backgroundMethod': 0}, 'viewerHL': 15, 'cameraMode': 'mono', 'detail': 5, 'viewerFog': None, 'viewerBG': 14}

	replyobj.status("Initializing session restore...", blankAfter=0,
		secondary=True)
	from SimpleSession.versions.v65 import expandSummary
	init(dict(enumerate(expandSummary(colorInfo))))
	replyobj.status("Restoring colors...", blankAfter=0,
		secondary=True)
	restoreColors(colors, materials)
	replyobj.status("Restoring molecules...", blankAfter=0,
		secondary=True)
	restoreMolecules(molInfo, resInfo, atomInfo, bondInfo, crdInfo)
	replyobj.status("Restoring surfaces...", blankAfter=0,
		secondary=True)
	restoreSurfaces(surfInfo)
	replyobj.status("Restoring VRML models...", blankAfter=0,
		secondary=True)
	restoreVRML(vrmlInfo)
	replyobj.status("Restoring pseudobond groups...", blankAfter=0,
		secondary=True)
	restorePseudoBondGroups(pbInfo)
	replyobj.status("Restoring model associations...", blankAfter=0,
		secondary=True)
	restoreModelAssociations(modelAssociations)
	replyobj.status("Restoring camera...", blankAfter=0,
		secondary=True)
	restoreViewer(viewerInfo)

try:
	restoreCoreModels()
except:
	reportRestoreError("Error restoring core models")

	replyobj.status("Restoring extension info...", blankAfter=0,
		secondary=True)


try:
	import StructMeasure
	from StructMeasure.DistMonitor import restoreDistances
	registerAfterModelsCB(restoreDistances, 1)
except:
	reportRestoreError("Error restoring distances in session")


def restoreMidasBase():
	formattedPositions = {}
	import Midas
	Midas.restoreMidasBase(formattedPositions)
try:
	restoreMidasBase()
except:
	reportRestoreError('Error restoring Midas base state')


def restoreMidasText():
	from Midas import midas_text
	midas_text.aliases = {'mmatch': 'hbonds intermodel false relax true angleSlop 40.0 color Blue linewidth 1.5; tile # spacingfactor 0.85 columns 2; color byhet;color red #0.1@O; color blue #0.2@O; color red #0.3@O; color red #0.4@O; color blue #0.5@O; color green #0.6@O', 'mylabel': 'labelopt info molecule; label offset 0,0.5,0 @/serialNumber=1; color black,al', 'simple': 'preset apply pub 1; light mode ambient; rep bs; set silhouette_width 3; setattr m stickScale .5; bondcolor black; color gray C', 'mytile': 'tile # spacingfactor $1 columns $2; color byhet', 'overlay': 'match #0.5 #0.3; match #0.6 #0.4; center; focus; preset apply pub 1', 'simpleWater': 'preset apply pub 1; light mode ambient; rep bs; set silhouette_width 3; setattr m stickScale .5; bondcolor gray; color red O; color white H', 'simpleB': 'preset apply pub 1; light mode ambient; rep bs; set silhouette_width 3; setattr m stickScale .5', 'pub1': 'preset apply pub 1', 'myhbonds': 'hbonds intermodel false relax true angleSlop 40.0 color Blue linewidth 2.5', 'MunkMatch': 'hbonds intermodel false ;tile # columns 2; match #0 #2  ; match #1 #3; center; focus; preset apply pub 1;color byhet', 'arrange': 'tile; center; focus'}
	midas_text.userSurfCategories = {}

try:
	restoreMidasText()
except:
	reportRestoreError('Error restoring Midas text state')


def restore_cap_attributes():
 cap_attributes = \
  {
   'cap_attributes': [
     {
      'cap_color': None,
      'class': 'Model_Capper_State',
      'display_style': None,
      'surface': ( 0, 0, ),
      'version': 1,
     },
     {
      'cap_color': None,
      'class': 'Model_Capper_State',
      'display_style': None,
      'surface': ( 1, 0, ),
      'version': 1,
     },
     {
      'cap_color': None,
      'class': 'Model_Capper_State',
      'display_style': None,
      'surface': ( 2, 0, ),
      'version': 1,
     },
     {
      'cap_color': None,
      'class': 'Model_Capper_State',
      'display_style': None,
      'surface': ( 3, 0, ),
      'version': 1,
     },
     {
      'cap_color': None,
      'class': 'Model_Capper_State',
      'display_style': None,
      'surface': ( 4, 0, ),
      'version': 1,
     },
     {
      'cap_color': None,
      'class': 'Model_Capper_State',
      'display_style': None,
      'surface': ( 5, 0, ),
      'version': 1,
     },
    ],
   'cap_color': None,
   'cap_offset': 0.01,
   'class': 'Caps_State',
   'default_cap_offset': 0.01,
   'mesh_style': False,
   'shown': True,
   'subdivision_factor': 1.0,
   'version': 1,
  }
 import SurfaceCap.session
 SurfaceCap.session.restore_cap_attributes(cap_attributes)
registerAfterModelsCB(restore_cap_attributes)


def restore_volume_data():
 volume_data_state = \
  {
   'class': 'Volume_Manager_State',
   'data_and_regions_state': [ ],
   'version': 2,
  }
 from VolumeViewer import session
 session.restore_volume_data_state(volume_data_state)

try:
  restore_volume_data()
except:
  reportRestoreError('Error restoring volume data')

geomData = {'AxisManager': {}, 'CentroidManager': {}, 'PlaneManager': {}}

try:
	from StructMeasure.Geometry import geomManager
	geomManager._restoreSession(geomData)
except:
	reportRestoreError("Error restoring geometry objects in session")


def restoreSession_RibbonStyleEditor():
	import SimpleSession
	import RibbonStyleEditor
	userScalings = [('licorice', [[0.35, 0.35], [0.35, 0.35], [0.35, 0.35], [0.35, 0.35, 0.35, 0.35], [0.35, 0.35]])]
	userXSections = []
	userResidueClasses = []
	residueData = [(6, 'Chimera default', 'rounded', u'unknown'), (7, 'Chimera default', 'rounded', u'unknown'), (8, 'Chimera default', 'rounded', u'unknown'), (9, 'Chimera default', 'rounded', u'unknown'), (10, 'Chimera default', 'rounded', u'unknown'), (11, 'Chimera default', 'rounded', u'unknown')]
	flags = RibbonStyleEditor.NucleicDefault1
	SimpleSession.registerAfterModelsCB(RibbonStyleEditor.restoreState,
				(userScalings, userXSections,
				userResidueClasses, residueData, flags))
try:
	restoreSession_RibbonStyleEditor()
except:
	reportRestoreError("Error restoring RibbonStyleEditor state")

trPickle = 'gAJjQW5pbWF0ZS5UcmFuc2l0aW9ucwpUcmFuc2l0aW9ucwpxASmBcQJ9cQMoVQxjdXN0b21fc2NlbmVxBGNBbmltYXRlLlRyYW5zaXRpb24KVHJhbnNpdGlvbgpxBSmBcQZ9cQcoVQZmcmFtZXNxCEsBVQ1kaXNjcmV0ZUZyYW1lcQlLAVUKcHJvcGVydGllc3EKXXELVQNhbGxxDGFVBG5hbWVxDWgEVQRtb2RlcQ5VBmxpbmVhcnEPdWJVCGtleWZyYW1lcRBoBSmBcRF9cRIoaAhLFGgJSwFoCl1xE2gMYWgNaBBoDmgPdWJVBXNjZW5lcRRoBSmBcRV9cRYoaAhLAWgJSwFoCl1xF2gMYWgNaBRoDmgPdWJ1Yi4='
scPickle = 'gAJjQW5pbWF0ZS5TY2VuZXMKU2NlbmVzCnEBKYFxAn1xA1UHbWFwX2lkc3EEfXNiLg=='
kfPickle = 'gAJjQW5pbWF0ZS5LZXlmcmFtZXMKS2V5ZnJhbWVzCnEBKYFxAn1xA1UHZW50cmllc3EEXXEFc2Iu'
def restoreAnimation():
	'A method to unpickle and restore animation objects'
	# Scenes must be unpickled after restoring transitions, because each
	# scene links to a 'scene' transition. Likewise, keyframes must be 
	# unpickled after restoring scenes, because each keyframe links to a scene.
	# The unpickle process is left to the restore* functions, it's 
	# important that it doesn't happen prior to calling those functions.
	import SimpleSession
	from Animate.Session import restoreTransitions
	from Animate.Session import restoreScenes
	from Animate.Session import restoreKeyframes
	SimpleSession.registerAfterModelsCB(restoreTransitions, trPickle)
	SimpleSession.registerAfterModelsCB(restoreScenes, scPickle)
	SimpleSession.registerAfterModelsCB(restoreKeyframes, kfPickle)
try:
	restoreAnimation()
except:
	reportRestoreError('Error in Animate.Session')

def restoreLightController():
	import Lighting
	Lighting._setFromParams({'ratio': 1.25, 'brightness': 1.16, 'material': [30.0, (0.85, 0.85, 0.85), 1.0], 'back': [(0.35740674433659325, 0.6604015517481454, -0.6604015517481455), (1.0, 1.0, 1.0), 0.0], 'mode': 'two-point', 'key': [(-0.35740674433659325, 0.6604015517481454, 0.6604015517481455), (1.0, 1.0, 1.0), 1.0], 'contrast': 0.83, 'fill': [(0.25056280708573153, 0.25056280708573153, 0.9351131265310293), (1.0, 1.0, 1.0), 0.0]})
try:
	restoreLightController()
except:
	reportRestoreError("Error restoring lighting parameters")


try:
	import Ilabel
	il = Ilabel.LabelsModel(create=False)
	if il:
		il.destroy()
	il = Ilabel.LabelsModel()
	il.restoreSession({'labelIDs': ['label2d_id_0', 'label2d_id_1', 'label2d_id_2', 'label2d_id_3', 'label2d_id_5'], 'curLabel': 4, 'labels': [{'opacity': 1.0, 'lines': [[{'args': (u'w',), 'kw': {'baselineOffset': 0, 'fontName': 'Sans Serif', 'style': 0, 'rgba': (0, 0, 1.0, 1.0), 'size': 24}}, {'args': (u'a',), 'kw': {'baselineOffset': 0, 'fontName': 'Sans Serif', 'style': 0, 'rgba': (0, 0, 1.0, 1.0), 'size': 24}}, {'args': (u't',), 'kw': {'baselineOffset': 0, 'fontName': 'Sans Serif', 'style': 0, 'rgba': (0, 0, 1.0, 1.0), 'size': 24}}, {'args': (u'e',), 'kw': {'baselineOffset': 0, 'fontName': 'Sans Serif', 'style': 0, 'rgba': (0, 0, 1.0, 1.0), 'size': 24}}, {'args': (u'r',), 'kw': {'baselineOffset': 0, 'fontName': 'Sans Serif', 'style': 0, 'rgba': (0, 0, 1.0, 1.0), 'size': 24}}, {'args': (u' ',), 'kw': {'baselineOffset': 0, 'fontName': 'Sans Serif', 'style': 0, 'rgba': (0, 0, 1.0, 1.0), 'size': 24}}, {'args': (u'c',), 'kw': {'baselineOffset': 0, 'fontName': 'Sans Serif', 'style': 0, 'rgba': (0, 0, 1.0, 1.0), 'size': 24}}, {'args': (u'l',), 'kw': {'baselineOffset': 0, 'fontName': 'Sans Serif', 'style': 0, 'rgba': (0, 0, 1.0, 1.0), 'size': 24}}, {'args': (u'u',), 'kw': {'baselineOffset': 0, 'fontName': 'Sans Serif', 'style': 0, 'rgba': (0, 0, 1.0, 1.0), 'size': 24}}, {'args': (u's',), 'kw': {'baselineOffset': 0, 'fontName': 'Sans Serif', 'style': 0, 'rgba': (0, 0, 1.0, 1.0), 'size': 24}}, {'args': (u't',), 'kw': {'baselineOffset': 0, 'fontName': 'Sans Serif', 'style': 0, 'rgba': (0, 0, 1.0, 1.0), 'size': 24}}, {'args': (u'e',), 'kw': {'baselineOffset': 0, 'fontName': 'Sans Serif', 'style': 0, 'rgba': (0, 0, 1.0, 1.0), 'size': 24}}, {'args': (u'r',), 'kw': {'baselineOffset': 0, 'fontName': 'Sans Serif', 'style': 0, 'rgba': (0, 0, 1.0, 1.0), 'size': 24}}, {'args': (u's',), 'kw': {'baselineOffset': 0, 'fontName': 'Sans Serif', 'style': 0, 'rgba': (0, 0, 1.0, 1.0), 'size': 24}}], []], 'shown': True, 'args': ((0.09765625, 0.5915492957746478),), 'kw': {'margin': 9, 'outline': 0, 'background': (1.0, 1.0, 0.037037037037037035, 0.75)}}, {'opacity': 1.0, 'lines': [[{'args': (u's',), 'kw': {'baselineOffset': 0, 'fontName': 'Sans Serif', 'style': 0, 'rgba': (0, 0, 1.0, 1.0), 'size': 24}}, {'args': (u'u',), 'kw': {'baselineOffset': 0, 'fontName': 'Sans Serif', 'style': 0, 'rgba': (0, 0, 1.0, 1.0), 'size': 24}}, {'args': (u'l',), 'kw': {'baselineOffset': 0, 'fontName': 'Sans Serif', 'style': 0, 'rgba': (0, 0, 1.0, 1.0), 'size': 24}}, {'args': (u'f',), 'kw': {'baselineOffset': 0, 'fontName': 'Sans Serif', 'style': 0, 'rgba': (0, 0, 1.0, 1.0), 'size': 24}}, {'args': (u'a',), 'kw': {'baselineOffset': 0, 'fontName': 'Sans Serif', 'style': 0, 'rgba': (0, 0, 1.0, 1.0), 'size': 24}}, {'args': (u't',), 'kw': {'baselineOffset': 0, 'fontName': 'Sans Serif', 'style': 0, 'rgba': (0, 0, 1.0, 1.0), 'size': 24}}, {'args': (u'e',), 'kw': {'baselineOffset': 0, 'fontName': 'Sans Serif', 'style': 0, 'rgba': (0, 0, 1.0, 1.0), 'size': 24}}, {'args': (u' ',), 'kw': {'baselineOffset': 0, 'fontName': 'Sans Serif', 'style': 0, 'rgba': (0, 0, 1.0, 1.0), 'size': 24}}, {'args': (u'h',), 'kw': {'baselineOffset': 0, 'fontName': 'Sans Serif', 'style': 0, 'rgba': (0, 0, 1.0, 1.0), 'size': 24}}, {'args': (u'y',), 'kw': {'baselineOffset': 0, 'fontName': 'Sans Serif', 'style': 0, 'rgba': (0, 0, 1.0, 1.0), 'size': 24}}, {'args': (u'd',), 'kw': {'baselineOffset': 0, 'fontName': 'Sans Serif', 'style': 0, 'rgba': (0, 0, 1.0, 1.0), 'size': 24}}, {'args': (u'r',), 'kw': {'baselineOffset': 0, 'fontName': 'Sans Serif', 'style': 0, 'rgba': (0, 0, 1.0, 1.0), 'size': 24}}, {'args': (u'a',), 'kw': {'baselineOffset': 0, 'fontName': 'Sans Serif', 'style': 0, 'rgba': (0, 0, 1.0, 1.0), 'size': 24}}, {'args': (u't',), 'kw': {'baselineOffset': 0, 'fontName': 'Sans Serif', 'style': 0, 'rgba': (0, 0, 1.0, 1.0), 'size': 24}}, {'args': (u'e',), 'kw': {'baselineOffset': 0, 'fontName': 'Sans Serif', 'style': 0, 'rgba': (0, 0, 1.0, 1.0), 'size': 24}}, {'args': (u's',), 'kw': {'baselineOffset': 0, 'fontName': 'Sans Serif', 'style': 0, 'rgba': (0, 0, 1.0, 1.0), 'size': 24}}], []], 'shown': True, 'args': ((0.5224609375, 0.5749039692701665),), 'kw': {'margin': 9, 'outline': 0, 'background': (1.0, 1.0, 0.037037037037037035, 0.75)}}, {'opacity': 1.0, 'lines': [[{'args': (u's',), 'kw': {'baselineOffset': 0, 'fontName': 'Sans Serif', 'style': 0, 'rgba': (0, 0, 1.0, 1.0), 'size': 24}}, {'args': (u'u',), 'kw': {'baselineOffset': 0, 'fontName': 'Sans Serif', 'style': 0, 'rgba': (0, 0, 1.0, 1.0), 'size': 24}}, {'args': (u'l',), 'kw': {'baselineOffset': 0, 'fontName': 'Sans Serif', 'style': 0, 'rgba': (0, 0, 1.0, 1.0), 'size': 24}}, {'args': (u'f',), 'kw': {'baselineOffset': 0, 'fontName': 'Sans Serif', 'style': 0, 'rgba': (0, 0, 1.0, 1.0), 'size': 24}}, {'args': (u'a',), 'kw': {'baselineOffset': 0, 'fontName': 'Sans Serif', 'style': 0, 'rgba': (0, 0, 1.0, 1.0), 'size': 24}}, {'args': (u't',), 'kw': {'baselineOffset': 0, 'fontName': 'Sans Serif', 'style': 0, 'rgba': (0, 0, 1.0, 1.0), 'size': 24}}, {'args': (u'e',), 'kw': {'baselineOffset': 0, 'fontName': 'Sans Serif', 'style': 0, 'rgba': (0, 0, 1.0, 1.0), 'size': 24}}, {'args': (u' ',), 'kw': {'baselineOffset': 0, 'fontName': 'Sans Serif', 'style': 0, 'rgba': (0, 0, 1.0, 1.0), 'size': 24}}, {'args': (u'a',), 'kw': {'baselineOffset': 0, 'fontName': 'Sans Serif', 'style': 0, 'rgba': (0, 0, 1.0, 1.0), 'size': 24}}, {'args': (u'e',), 'kw': {'baselineOffset': 0, 'fontName': 'Sans Serif', 'style': 0, 'rgba': (0, 0, 1.0, 1.0), 'size': 24}}, {'args': (u'r',), 'kw': {'baselineOffset': 0, 'fontName': 'Sans Serif', 'style': 0, 'rgba': (0, 0, 1.0, 1.0), 'size': 24}}, {'args': (u'o',), 'kw': {'baselineOffset': 0, 'fontName': 'Sans Serif', 'style': 0, 'rgba': (0, 0, 1.0, 1.0), 'size': 24}}, {'args': (u's',), 'kw': {'baselineOffset': 0, 'fontName': 'Sans Serif', 'style': 0, 'rgba': (0, 0, 1.0, 1.0), 'size': 24}}, {'args': (u'o',), 'kw': {'baselineOffset': 0, 'fontName': 'Sans Serif', 'style': 0, 'rgba': (0, 0, 1.0, 1.0), 'size': 24}}, {'args': (u'l',), 'kw': {'baselineOffset': 0, 'fontName': 'Sans Serif', 'style': 0, 'rgba': (0, 0, 1.0, 1.0), 'size': 24}}, {'args': (u's',), 'kw': {'baselineOffset': 0, 'fontName': 'Sans Serif', 'style': 0, 'rgba': (0, 0, 1.0, 1.0), 'size': 24}}]], 'shown': True, 'args': ((0.087890625, 0.0793854033290653),), 'kw': {'margin': 9, 'outline': 0, 'background': (1.0, 1.0, 0.037037037037037035, 0.75)}}, {'opacity': 1.0, 'lines': [[{'args': (u'w',), 'kw': {'baselineOffset': 0, 'fontName': 'Sans Serif', 'style': 0, 'rgba': (0, 0, 1.0, 1.0), 'size': 24}}, {'args': (u'a',), 'kw': {'baselineOffset': 0, 'fontName': 'Sans Serif', 'style': 0, 'rgba': (0, 0, 1.0, 1.0), 'size': 24}}, {'args': (u't',), 'kw': {'baselineOffset': 0, 'fontName': 'Sans Serif', 'style': 0, 'rgba': (0, 0, 1.0, 1.0), 'size': 24}}, {'args': (u'e',), 'kw': {'baselineOffset': 0, 'fontName': 'Sans Serif', 'style': 0, 'rgba': (0, 0, 1.0, 1.0), 'size': 24}}, {'args': (u'r',), 'kw': {'baselineOffset': 0, 'fontName': 'Sans Serif', 'style': 0, 'rgba': (0, 0, 1.0, 1.0), 'size': 24}}, {'args': (u' ',), 'kw': {'baselineOffset': 0, 'fontName': 'Sans Serif', 'style': 0, 'rgba': (0, 0, 1.0, 1.0), 'size': 24}}, {'args': (u'+',), 'kw': {'baselineOffset': 0, 'fontName': 'Sans Serif', 'style': 0, 'rgba': (0, 0, 1.0, 1.0), 'size': 24}}, {'args': (u' ',), 'kw': {'baselineOffset': 0, 'fontName': 'Sans Serif', 'style': 0, 'rgba': (0, 0, 1.0, 1.0), 'size': 24}}, {'args': (u'p',), 'kw': {'baselineOffset': 0, 'fontName': 'Sans Serif', 'style': 0, 'rgba': (0, 0, 1.0, 1.0), 'size': 24}}, {'args': (u'o',), 'kw': {'baselineOffset': 0, 'fontName': 'Sans Serif', 'style': 0, 'rgba': (0, 0, 1.0, 1.0), 'size': 24}}, {'args': (u'l',), 'kw': {'baselineOffset': 0, 'fontName': 'Sans Serif', 'style': 0, 'rgba': (0, 0, 1.0, 1.0), 'size': 24}}, {'args': (u'y',), 'kw': {'baselineOffset': 0, 'fontName': 'Sans Serif', 'style': 0, 'rgba': (0, 0, 1.0, 1.0), 'size': 24}}, {'args': (u'a',), 'kw': {'baselineOffset': 0, 'fontName': 'Sans Serif', 'style': 0, 'rgba': (0, 0, 1.0, 1.0), 'size': 24}}, {'args': (u'r',), 'kw': {'baselineOffset': 0, 'fontName': 'Sans Serif', 'style': 0, 'rgba': (0, 0, 1.0, 1.0), 'size': 24}}, {'args': (u'o',), 'kw': {'baselineOffset': 0, 'fontName': 'Sans Serif', 'style': 0, 'rgba': (0, 0, 1.0, 1.0), 'size': 24}}, {'args': (u'm',), 'kw': {'baselineOffset': 0, 'fontName': 'Sans Serif', 'style': 0, 'rgba': (0, 0, 1.0, 1.0), 'size': 24}}, {'args': (u'a',), 'kw': {'baselineOffset': 0, 'fontName': 'Sans Serif', 'style': 0, 'rgba': (0, 0, 1.0, 1.0), 'size': 24}}, {'args': (u't',), 'kw': {'baselineOffset': 0, 'fontName': 'Sans Serif', 'style': 0, 'rgba': (0, 0, 1.0, 1.0), 'size': 24}}, {'args': (u'i',), 'kw': {'baselineOffset': 0, 'fontName': 'Sans Serif', 'style': 0, 'rgba': (0, 0, 1.0, 1.0), 'size': 24}}, {'args': (u'c',), 'kw': {'baselineOffset': 0, 'fontName': 'Sans Serif', 'style': 0, 'rgba': (0, 0, 1.0, 1.0), 'size': 24}}, {'args': (u' ',), 'kw': {'baselineOffset': 0, 'fontName': 'Sans Serif', 'style': 0, 'rgba': (0, 0, 1.0, 1.0), 'size': 24}}, {'args': (u'h',), 'kw': {'baselineOffset': 0, 'fontName': 'Sans Serif', 'style': 0, 'rgba': (0, 0, 1.0, 1.0), 'size': 24}}, {'args': (u'y',), 'kw': {'baselineOffset': 0, 'fontName': 'Sans Serif', 'style': 0, 'rgba': (0, 0, 1.0, 1.0), 'size': 24}}, {'args': (u'd',), 'kw': {'baselineOffset': 0, 'fontName': 'Sans Serif', 'style': 0, 'rgba': (0, 0, 1.0, 1.0), 'size': 24}}, {'args': (u'r',), 'kw': {'baselineOffset': 0, 'fontName': 'Sans Serif', 'style': 0, 'rgba': (0, 0, 1.0, 1.0), 'size': 24}}, {'args': (u'o',), 'kw': {'baselineOffset': 0, 'fontName': 'Sans Serif', 'style': 0, 'rgba': (0, 0, 1.0, 1.0), 'size': 24}}, {'args': (u'c',), 'kw': {'baselineOffset': 0, 'fontName': 'Sans Serif', 'style': 0, 'rgba': (0, 0, 1.0, 1.0), 'size': 24}}, {'args': (u'a',), 'kw': {'baselineOffset': 0, 'fontName': 'Sans Serif', 'style': 0, 'rgba': (0, 0, 1.0, 1.0), 'size': 24}}, {'args': (u'r',), 'kw': {'baselineOffset': 0, 'fontName': 'Sans Serif', 'style': 0, 'rgba': (0, 0, 1.0, 1.0), 'size': 24}}, {'args': (u'b',), 'kw': {'baselineOffset': 0, 'fontName': 'Sans Serif', 'style': 0, 'rgba': (0, 0, 1.0, 1.0), 'size': 24}}, {'args': (u'o',), 'kw': {'baselineOffset': 0, 'fontName': 'Sans Serif', 'style': 0, 'rgba': (0, 0, 1.0, 1.0), 'size': 24}}, {'args': (u'n',), 'kw': {'baselineOffset': 0, 'fontName': 'Sans Serif', 'style': 0, 'rgba': (0, 0, 1.0, 1.0), 'size': 24}}, {'args': (u's',), 'kw': {'baselineOffset': 0, 'fontName': 'Sans Serif', 'style': 0, 'rgba': (0, 0, 1.0, 1.0), 'size': 24}}, {'args': (u' ',), 'kw': {'baselineOffset': 0, 'fontName': 'Sans Serif', 'style': 0, 'rgba': (0, 0, 1.0, 1.0), 'size': 24}}, {'args': (u'(',), 'kw': {'baselineOffset': 0, 'fontName': 'Sans Serif', 'style': 0, 'rgba': (0, 0, 1.0, 1.0), 'size': 24}}, {'args': (u'P',), 'kw': {'baselineOffset': 0, 'fontName': 'Sans Serif', 'style': 0, 'rgba': (0, 0, 1.0, 1.0), 'size': 24}}, {'args': (u'A',), 'kw': {'baselineOffset': 0, 'fontName': 'Sans Serif', 'style': 0, 'rgba': (0, 0, 1.0, 1.0), 'size': 24}}, {'args': (u'H',), 'kw': {'baselineOffset': 0, 'fontName': 'Sans Serif', 'style': 0, 'rgba': (0, 0, 1.0, 1.0), 'size': 24}}, {'args': (u')',), 'kw': {'baselineOffset': 0, 'fontName': 'Sans Serif', 'style': 0, 'rgba': (0, 0, 1.0, 1.0), 'size': 24}}]], 'shown': True, 'args': ((0.46484375, 0.09218950064020487),), 'kw': {'margin': 9, 'outline': 0, 'background': (1.0, 1.0, 0.037037037037037035, 0.75)}}, {'opacity': 1.0, 'lines': [[]], 'shown': True, 'args': ((0.0615234375, 0.998719590268886),), 'kw': {'margin': 9.0, 'outline': 0.0, 'background': None}}], 'labelUID': 6})
	del Ilabel, il
except:
	reportRestoreError("Error restoring IlabelModel instance in session")


try:
	from Ilabel.Arrows import ArrowsModel
	ArrowsModel().restore({'arrows': []})
except:
	reportRestoreError("Error restoring 2D arrows in session")



try:
	from Ilabel.ColorKey import getKeyModel
	getKeyModel()._restoreSession({'label spacing': 'proportional to value', 'label justification': 'decimal point', 'font size': 24, 'label positions': 'right/bottom', 'show ticks': False, 'border width': 2, 'label offset': 0, 'color depiction': 'blended', 'label color': (0, 0, 0), 'font name': 'Sans Serif', 'tick length': 10, 'border color': (0, 0, 0, 1.0), 'key position': None, 'font typeface': 0, 'tick thickness': 4, 'colors/labels': [((0, 0, 1, 1), 'min'), ((1, 1, 1, 1), ''), ((1, 0, 0, 1), 'max')]})
except:
	reportRestoreError("Error restoring color key")



def restore2DLabelDialog(info):
	from chimera.dialogs import find
	from Ilabel.gui import IlabelDialog
	dlg = find(IlabelDialog.name)
	if dlg is not None:
		dlg.destroy()
	dlg = find(IlabelDialog.name, create=True)
	dlg._restoreSession(info)

import SimpleSession
SimpleSession.registerAfterModelsCB(restore2DLabelDialog, {'mouse func': 'labeling', 'sel ranges': (), 'dialog shown': 1})



def restoreRemainder():
	from SimpleSession.versions.v65 import restoreWindowSize, \
	     restoreOpenStates, restoreSelections, restoreFontInfo, \
	     restoreOpenModelsAttrs, restoreModelClip, restoreSilhouettes

	curSelIds =  []
	savedSels = []
	openModelsAttrs = { 'cofrMethod': 2 }
	windowSize = (1024, 781)
	xformMap = {0: (((-0.34821455627968, 0.82726846257295, 0.44087811652103), 9.9995089373332), (0.0076537672682732, 0.0083331466146478, -0.0095913043915013), False), 1: (((-0.99040907112338, 0.13815836179107, 0.0014624991412663), 109.62935189875), (8.9189222591104, -0.045770457294621, -0.032931556893357), False), 2: (((-0.20080631594196, -0.92498261478313, 0.32262049815036), 18.985788096111), (17.497129733092, -0.68455407611151, -0.47980035902674), False), 3: (((0.99205523056863, 0.020289399059421, -0.12415619109504), 170.88474103051), (-0.1169711633136, -8.6869766220186, 0.11207397706245), True), 4: (((0.23529125830917, 0.94204993508282, 0.23912328112031), 96.859237242746), (8.9195514371968, -9.2219927891895, -0.28512231169757), False), 5: (((0.73008849334292, 0.68289739957367, 0.024938595465521), 170.41609346508), (18.067194686271, -9.1650094893277, -1.4626137937459), False)}
	fontInfo = {'face': (u'Sans Serif', 'Bold', 12)}
	clipPlaneInfo = {}
	silhouettes = {0: True, 1: True, 2: True, 3: True, 4: True, 5: True, 294: True, 289: True, 323: True, 322: True, 290: True, 291: True, 292: True, 293: True}

	replyobj.status("Restoring window...", blankAfter=0,
		secondary=True)
	restoreWindowSize(windowSize)
	replyobj.status("Restoring open states...", blankAfter=0,
		secondary=True)
	restoreOpenStates(xformMap)
	replyobj.status("Restoring font info...", blankAfter=0,
		secondary=True)
	restoreFontInfo(fontInfo)
	replyobj.status("Restoring selections...", blankAfter=0,
		secondary=True)
	restoreSelections(curSelIds, savedSels)
	replyobj.status("Restoring openModel attributes...", blankAfter=0,
		secondary=True)
	restoreOpenModelsAttrs(openModelsAttrs)
	replyobj.status("Restoring model clipping...", blankAfter=0,
		secondary=True)
	restoreModelClip(clipPlaneInfo)
	replyobj.status("Restoring per-model silhouettes...", blankAfter=0,
		secondary=True)
	restoreSilhouettes(silhouettes)

	replyobj.status("Restoring remaining extension info...", blankAfter=0,
		secondary=True)
try:
	restoreRemainder()
except:
	reportRestoreError("Error restoring post-model state")
from SimpleSession.versions.v65 import makeAfterModelsCBs
makeAfterModelsCBs()

from SimpleSession.versions.v65 import endRestore
replyobj.status('Finishing restore...', blankAfter=0, secondary=True)
endRestore({})
replyobj.status('', secondary=True)
replyobj.status('Restore finished.')

