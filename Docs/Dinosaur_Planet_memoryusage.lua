console.log(string.format("mem (%d / %d) (%d / %d) (%d / %d)",
	mainmemory.read_u32_be(0x08EAA0), mainmemory.read_u32_be(0x0B09DC),
	mainmemory.read_u32_be(0x08EAA4), mainmemory.read_u32_be(0x0B09F0),
	mainmemory.read_u32_be(0x08EAA8), mainmemory.read_u32_be(0x0B0A04)))
	
console.log(string.format("slot (%d / %d) (%d / %d) (%d / %d)",
	mainmemory.read_u32_be(0x0B09D4), mainmemory.read_u32_be(0x0B09D0),
	mainmemory.read_u32_be(0x0B09E8), mainmemory.read_u32_be(0x0B09E4),
	mainmemory.read_u32_be(0x0B09FC), mainmemory.read_u32_be(0x0B09F8)))