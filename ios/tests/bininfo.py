## fufluns - Copyright 2019 - deroad

def run_tests(o, r2, u, r2h):
	filename = r2h.filename(r2)
	o.binary.hashes(filename, r2h.cmdj(r2, 'itj'))
	o.binary.libraries(r2h.cmdj(r2, 'ilj'))
	o.binary.classes(filename, r2h.cmdj(r2, 'icj'))

def name_test():
	return "Hashes and binary details"