#Problem link:https://www.hackerrank.com/challenges/designer-pdf-viewer/problem
#Problem name:Designer PDF Viewer
#Status: Easy
#Solution

def designerPdfViewer(h, word):
    st=string.ascii_lowercase
    l=list(st)
    length=len(word)
    maxh=0
    for i in word:
        j=l.index(i)
        maxh=max(maxh,h[j])
    return(maxh*length)
