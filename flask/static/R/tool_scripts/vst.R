# Performs VST.
#######################################################
########## 1. Libraries ###############################
#######################################################
suppressWarnings(suppressMessages(require(DESeq2)))

#######################################################
########## 2. Run #####################################
#######################################################

run_vst <- function(rawcount_dataframe) {
	# Calculate VST
	vst_dataframe <- as.data.frame(varianceStabilizingTransformation(as.matrix(rawcount_dataframe)))
	return(vst_dataframe)
}
