--------------------------------------------------------------
-- This file contains a LUCCME APPLICATION MODEL definition --
--               Compatible with LuccME 3.1                 --
--        Generated with LuccMe Model Configurator          --
--               12/11/2024 at 13:24:51                     --
--------------------------------------------------------------

--------------------------------------------------------------
-- Creating Terraview Project                               --
--------------------------------------------------------------

import("gis")

local projFile = File("t3mp.tview")
if(projFile:exists()) then
	projFile:delete()
end

proj = Project {
	file = "t3mp.tview",
	clean = true
}

l1 = Layer{
	project = proj,
	name = "layer",
	file = "../data/cs_moju/cs_moju.shp"
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
	startTime = 1999,
	endTime = 2004,

	-----------------------------------------------------
	-- Spatial dimension definition                    --
	-----------------------------------------------------
	cs = CellularSpace
	{
		project = "t3mp.tview",
		layer = "layer",
		cellArea = 1,
		xy = {"col", "lin"},
	},

	-----------------------------------------------------
	-- Land use variables definition                   --
	-----------------------------------------------------
	landUseTypes =
	{
		"f", "d", "o"
	},

	landUseNoData = "o",

	-----------------------------------------------------
	-- Behaviour dimension definition:                 --
	-- DEMAND, POTENTIAL AND ALLOCATION COMPONENTS     --
	-----------------------------------------------------
	demand = D1,
	potential = P1,
	allocation = A1,

	save  =
	{
		outputTheme = "Lab1_",
		mode = "multiple",
		saveYears = {2002, 2003, 2004},
		saveAttrs = 
		{
			"d_out",
			"f_out",
		},

	},

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
	--tsave = databaseSave(Lab1)
	--env_Lab1:add(tsave)

	env_Lab1:run(Lab1.endTime)



	saveSingleTheme(Lab1, true)
	projFile = File("t3mp.tview")
	if(projFile:exists()) then
		projFile:delete()
	end
end


