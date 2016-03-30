from enum import Enum

LineNames = {1:'Title1', 2:'TimeStamp', 3:'Ignore',

	#Extruder	
	4:'processName', 5:'applyToModels', 6:'profileName', 7:'profileVersion', 8:'baseProfile', 9:'printMaterial', 10:'printQuality', 11:'printExtruders', 12:'extruderName', 13:'extruderToolheadNumber', 14:'extruderDiameter', 15:'extruderAutoWidth', 16:'extruderWidth', 17:'extrusionMultiplier', 18:'extruderUseRetract', 19:'extruderRetractionDistance', 20:'extruderExtraRestartDistance', 21:'extruderRetractionZLift', 22:'extruderRetractionSpeed', 23:'extruderUseCoasting', 24:'extruderCoastingDistance', 25:'extruderUseWipe', 26:'extruderWipeDistance', 27:'primaryExtruder', 		#Layer	
	28:'layerHeight', 29:'topSolidLayers', 30:'bottomSolidLayers', 31:'perimeterOutlines', 32:'printPerimetersInsideOut', 33:'startPointOption', 34:'startPointOriginX', 35:'startPointOriginY', 36:'startPointOriginZ', 37:'sequentialIslands', 38:'spiralVaseMode', 39:'firstLayerHeightPercentage', 40:'firstLayerWidthPercentage', 41:'firstLayerUnderspeed', 

	#Additions', 
	42:'useRaft', 43:'raftExtruder', 44:'raftLayers', 45:'raftOffset', 46:'raftSeparationDistance', 47:'raftInfill', 48:'disableRaftBaseLayers', 49:'useSkirt', 50:'skirtExtruder', 51:'skirtLayers', 52:'skirtOutlines', 53:'skirtOffset', 54:'usePrimePillar', 55:'primePillarExtruder', 56:'primePillarWidth', 57:'primePillarLocation', 58:'primePillarSpeedMultiplier', 59:'useOozeShield', 60:'oozeShieldExtruder', 61:'oozeShieldOffset', 62:'oozeShieldOutlines', 63:'oozeShieldSidewallShape', 64:'oozeShieldSidewallAngle', 65:'oozeShieldSpeedMultiplier', 

	#Infill	
	66:'infillExtruder', 67:'internalInfillPattern', 68:'externalInfillPattern', 69:'infillPercentage', 70:'outlineOverlapPercentage', 71:'infillExtrusionWidthPercentage', 72:'minInfillLength', 73:'infillLayerInterval', 74:'infillAngles', 75:'overlapInfillAngles',

	#support	
	76:'generateSupport', 77:'supportExtruder', 78:'supportInfillPercentage', 79:'supportExtraInflation', 80:'denseSupportLayers', 81:'denseSupportInfillPercentage', 82:'supportLayerInterval', 83:'supportHorizontalPartOffset', 84:'supportUpperSeparationLayers', 85:'supportLowerSeparationLayers', 86:'supportType', 87:'supportGridSpacing', 88:'maxOverhangAngle', 89:'supportAngles', 

	#Temperature	
	90:'temperatureName', 91:'temperatureNumber', 92:'temperatureSetpointCount', 93:'temperatureSetpointLayers', 94:'temperatureSetpointTemperatures', 95:'temperatureStabilizeAtStartup', 96:'temperatureHeatedBed', 97:'temperatureRelayBetweenLayers', 98:'temperatureRelayBetweenLoops', 

	#cooling	
	99:'fanLayers', 100:'fanSpeeds', 101:'blipFanToFullPower', 102:'adjustSpeedForCooling', 103:'minSpeedLayerTime', 104:'minCoolingSpeedSlowdown', 105:'increaseFanForCooling', 106:'minFanLayerTime', 107:'maxCoolingFanSpeed', 108:'increaseFanForBridging', 109:'bridgingFanSpeed', 

	#Gcode	
	110:'use5D', 111:'relativeEdistances', 112:'allowEaxisZeroing', 113:'independentExtruderAxes', 114:'includeM10123', 115:'stickySupport', 116:'applyToolheadOffsets', 117:'gcodeXoffset', 118:'gcodeYoffset', 119:'gcodeZoffset', 120:'overrideMachineDefinition', 121:'machineTypeOverride', 122:'strokeXoverride', 123:'strokeYoverride', 124:'strokeZoverride', 125:'originOffsetXoverride', 126:'originOffsetYoverride', 127:'originOffsetZoverride', 128:'homeXdirOverride', 129:'homeYdirOverride', 130:'homeZdirOverride', 131:'flipXoverride', 132:'flipYoverride', 133:'flipZoverride', 134:'toolheadOffsets', 135:'overrideFirmwareConfiguration', 136:'firmwareTypeOverride', 137:'GPXconfigOverride', 138:'baudRateOverride',
	
	#Scripts
	139:'overridePrinterModels', 140:'printerModelsOverride', 141:'startingGcode', 142:'layerChangeGcode', 143:'retractionGcode', 144:'toolChangeGcode', 145:'endingGcode', 146:'createX3G', 147:'celebration', 148:'celebrationSong', 149:'createMB5G', 150:'postProcessing',

	#Other
	151:'defaultSpeed', 152:'outlineUnderspeed', 153:'solidInfillUnderspeed', 154:'supportUnderspeed', 155:'rapidXYspeed', 156:'rapidZspeed', 157:'minBridgingArea', 158:'bridgingExtraInflation', 159:'bridgingExtrusionMultiplier', 160:'bridgingSpeedMultiplier', 161:'filamentDiameter', 162:'filamentPricePerKg', 163:'filamentDensity',

	#Advanced
	164:'useMinPrintHeight', 165:'minPrintHeight', 166:'useMaxPrintHeight', 167:'maxPrintHeight', 168:'useDiaphragm', 169:'diaphragmLayerInterval', 170:'robustSlicing', 171:'mergeAllIntoSolid', 172:'onlyRetractWhenCrossingOutline', 173:'retractBetweenLayers', 174:'useRetractionMinTravel', 175:'retractionMinTravel', 176:'retractWhileWiping', 177:'onlyWipeOutlines', 178:'avoidCrossingOutline', 179:'maxMovementDetourFactor', 180:'toolChangeRetractionDistance', 181:'toolChangeExtraRestartDistance', 182:'toolChangeRetractionSpeed', 183:'allowThinWallGapFill', 184:'thinWallAllowedOverlapPercentage', 185:'horizontalSizeCompensation'}
	
#for looking up the next tab to switch on by line number
tabSwitchNum = {3:'Info', 26:'Extruder', 41:'Layer', 65:'Additions', 75:'Infill', 89:'Support', 98:'Temperature', 109:'Cooling',
 138:'GCode', 150:'Scripts', 163:'Other', 184:'Advanced'} #- 1 value is last but appears on this tab "hoizontalSizeCompensation"
 
#for looking up the next number to switch on by tab name
tabSwitchName = {'Info':3,'Extruder':26, 'Layer':41,  'Additions':65,  'Infill':75,  'Support':89,  'Temperature':98, 'Cooling':109,  'GCode':138,  'Scripts':150,  'Other':163,  'Advanced':184, } #'Other':185 Must be manual
 
class TabEnum(Enum):
	Info = 0
	Extruder = 1
	Layer = 2
	Additions = 3
	Infill = 4
	Support = 5
	Temperature = 6
	Cooling = 7
	GCode = 8
	Scripts = 9
	Other = 10
	Advanced = 11
	#Info = 12
	#Console = 13
	
	def describe(self):
		return self.name, self.value
		
	def __str__(self):
		return '{0}'.format(self.name)
		
	@property
	def getTabValue(self):
		retStr = TabEnum(self.tabNum)
		return retStr
