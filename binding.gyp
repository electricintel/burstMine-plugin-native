{
	"targets":[
		{
			"target_name":"burstMine-plugin-native",
			"include_dirs":[
				"../../../src"
			],
			"sources":[
				"../../../src/burstMine/ScoopsBuffer.cpp",
				"../../../src/burstMine/Plots.cpp",
				"../../../src/burstMine/PlotsStaggered.cpp",
				"../../../src/burstMine/PlotsWriter.cpp",
				"../../../src/burstMine/PlotsWriterStaggered.cpp",
				"../../../src/burstMine/js/JsScoopsBuffer.cpp",
				"../../../src/burstMine/js/JsPlots.cpp",
				"../../../src/burstMine/js/JsPlotsStaggered.cpp",
				"../../../src/burstMine/js/impl/AsyncData.cpp",
				"src/burstMine/plugins/native/PlotsStaggeredFile.cpp",
				"src/burstMine/plugins/native/PlotsWriterStaggeredFile.cpp",
				"src/burstMine/plugins/native/js/JsPlotsStaggeredFile.cpp",
				"src/burstMine/plugins/native/js/JsPlotsWriterStaggeredFile.cpp",
				"src/burstMine/plugins/native/js/JsPluginNative.cpp"
			],
			"conditions":[
				["OS == 'win'", {
					"configurations":{
						"Release":{
							"msvs_settings":{
								"VCCLCompilerTool":{
									"ExceptionHandling":1,
									"DisableSpecificWarnings":["4290"]
								}
							}
						}
					}
				}]
			]
		},
		{
			"target_name":"post-build",
			"type":"none",
			"dependencies":["burstMine-plugin-native"],
			"copies":[
				{
					"files":["<(PRODUCT_DIR)/burstMine-plugin-native.node"],
					"destination":"bin"
				}
			]
		}
	]
}