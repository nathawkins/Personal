for imagename in `sudo tmutil listlocalsnapshots /`; do
#	tmutil deletelocalsnapshots $imagename[21:]
	tmutil deletelocalsnapshots  ${imagename:22}
done
