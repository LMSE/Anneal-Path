#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#
library(hypergraph)
library(hyperdraw)

DHE0000 <- DirectedHyperedge(c("(S)-Mevalonate"), c("C=C(C)CCO"), "EC4.1.1_0")
DHE0001 <- DirectedHyperedge(c("Mevaldate"), c("(S)-Mevalonate"), "EC1.1.1_0")
DHE0002 <- DirectedHyperedge(c("Acetaldehyde","Acetoacetate"), c("Mevaldate"), "EC4.1.2_0")
DHE0003 <- DirectedHyperedge(c("3-Oxobutanamide"), c("Acetoacetate"), "EC3.5.1_0")
DHE0004 <- DirectedHyperedge(c("NC(=O)CC(=O)CC=O"), c("NC(=O)CC(=O)O","Acetaldehyde"), "EC3.7.1_0")
DHE0005 <- DirectedHyperedge(c("NC(=O)CC(N)CC=O"), c("NC(=O)CC(=O)CC=O"), "EC1.4.1_0")
DHE0006 <- DirectedHyperedge(c("NC(=O)CC(=O)CC(=O)O"), c("HCO3-","3-Oxobutanamide"), "EC6.4.1_0")
DHE0007 <- DirectedHyperedge(c("NC(=O)CC(N)CC(=O)O"), c("NC(=O)CC(N)CC=O"), "EC1.2.1_0")
DHE0008 <- DirectedHyperedge(c("NC(=O)CC(N)CC(=O)O"), c("NC(=O)CC(=O)CC(=O)O"), "EC1.4.1_1")
DHE0009 <- DirectedHyperedge(c("Glutamine"), c("NC(=O)CC(N)CC(=O)O"), "EC5.4.3_0")
Cnodes <- c("(S)-Mevalonate","C=C(C)CCO","Mevaldate","Acetaldehyde","Acetoacetate","3-Oxobutanamide","NC(=O)CC(=O)CC=O","NC(=O)CC(=O)O","NC(=O)CC(N)CC=O","NC(=O)CC(=O)CC(=O)O","HCO3-","NC(=O)CC(N)CC(=O)O","Glutamine")
Rnodes <- list(DHE0000,DHE0001,DHE0002,DHE0003,DHE0004,DHE0005,DHE0006,DHE0007,DHE0008,DHE0009)
hg <- Hypergraph(Cnodes,Rnodes)
hgbph <- graphBPH(hg)
testrabph <- graphLayout(hgbph)
edgeDataDefaults(testrabph, "lwd") <- 1
edgeDataDefaults(testrabph, "color") <- "black"
nodeDataDefaults(testrabph, "margin") <- 'unit(1, "mm")'
nodeDataDefaults(testrabph, "shape") <- "box"
nodeDataDefaults(testrabph, "color") <- "black"
#plot(testrabph)
initial.options <- commandArgs(trailingOnly = FALSE)
file.arg.name <- "--file="
script.name <- sub(file.arg.name, "", initial.options[grep(file.arg.name, initial.options)])
script.basename <- dirname(script.name)
other.name <- file.path(script.basename, "")
save_path<-paste(other.name,"/pathways/pathway","5.png",sep="")
png(file = save_path, width = 1920, height = 1080, res = 300)
plot(testrabph)
dev.off()
