import facemorpher

imgpaths = facemorpher.list_imgpaths('imagpath')
facemorpher.averager(list(imgpaths), blur_edges=True, plot=True, background='black', width=1000, height=1000)