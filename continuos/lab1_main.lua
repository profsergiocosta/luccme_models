--------------------------------------------------------------
-- This file contains a LUCCME APPLICATION MODEL definition --
--               Compatible with LuccME 3.1                 --
--        Generated with LuccMe Model Configurator          --
--               11/11/2024 at 16:08:02                     --
--------------------------------------------------------------

--------------------------------------------------------------
-- Creating Terraview Project                               --
--------------------------------------------------------------

import("gis")


local projFile = File("projeto_apagar.tview")
if(projFile:exists()) then
	projFile:delete()
end


proj = Project {
	file = "projeto_apagar.tview",
	clean = true
}

l1 = Layer{
	project = proj,
	name = "csAC",
	file = "../data/cs_ac/csAC.shp"
}

--------------------------------------------------------------
-- LuccME Model                                             --
--------------------------------------------------------------

import("luccme")

dofile("lab1_submodel.lua")


--------------------------------------------------------------
-- LuccME APPLICATION MODEL DEFINITION                      --
--------------------------------------------------------------
Lab1 = LuccMEModel
{
	name = "Lab1",

	-----------------------------------------------------
	-- Temporal dimension definition                   --
	-----------------------------------------------------
	startTime = 2008,
	endTime = 2014,

	-----------------------------------------------------
	-- Spatial dimension definition                    --
	-----------------------------------------------------
	cs = CellularSpace
	{
		project = proj,
		layer = "csAC",
		cellArea = 25,
	},

	-----------------------------------------------------
	-- Land use variables definition                   --
	-----------------------------------------------------
	landUseTypes =
	{
		"f", "d", "outros"
	},

	landUseNoData = "outros",

	-----------------------------------------------------
	-- Behaviour dimension definition:                 --
	-- DEMAND, POTENTIAL AND ALLOCATION COMPONENTS     --
	-----------------------------------------------------
	demand = D1,
	potential = P1,
	allocation = A1,

	save  =
	{
		outputTheme = "../tmp/Lab1_",
		mode = "multiple",
		saveYears = {2013, 2014},
		saveAttrs = 
		{
			"f_out",
			"d_out",
			"outros_out",
		},

	},

	hasAuxiliaryOutputs = true,
	isCoupled = false
}  -- END LuccME application model definition

-----------------------------------------------------
-- ENVIROMMENT DEFINITION                          --
-----------------------------------------------------
timer = Timer
{
	Event
	{
		start = Lab1.startTime,
		action = function(event)
					Lab1:run(event)
					
				  end
	}
}

env_Lab1 = Environment{}
env_Lab1:add(timer)

-----------------------------------------------------
-- ENVIROMMENT EXECUTION                           --
-----------------------------------------------------

if Lab1.isCoupled == false then
	tsave = databaseSave(Lab1)
	env_Lab1:add(tsave)
	env_Lab1:run(Lab1.endTime)
	saveSingleTheme(Lab1, true)
	projFile = File("projeto_apagar.tview")
	if(projFile:exists()) then
		projFile:delete()
	end
end

--Lab1.cs:save("novo_1",  {"f"})