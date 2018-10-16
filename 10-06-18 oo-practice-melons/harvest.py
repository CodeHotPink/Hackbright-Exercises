############
# Part 1   #
############


class MelonType(object):
	"""A species of melon at a melon farm."""

	def __init__(self, code, name, first_harvest, color, is_seedless, is_bestseller):
		"""Initialize a melon."""
		self.code = code
		self.name = name
		self.first_harvest = first_harvest
		self.color = color
		self.is_seedless = is_seedless
		self.is_bestseller = is_bestseller

		self.pairings = []

	def add_pairing(self, pairing):
		"""Add a food pairing to the instance's pairings list."""
		self.pairings.append(pairing)

	def update_code(self, new_code):
		"""Replace the reporting code with the new_code."""
		self.code = new_code


def make_melon_types():
	"""Returns a list of current melon types."""
	all_melon_types = []

	musk = MelonType('musk', "muskmelon", 1998, 'green', True, True)
	musk.add_pairing("mint")
	all_melon_types.append(musk)

	cas = MelonType('cas', "casaba", 2003, 'orange', False, False)
	cas.add_pairing("mint")
	cas.add_pairing("strawberries")
	all_melon_types.append(cas)

	cren = MelonType('cren', "crenshaw", 1996, 'green', False, False)
	cren.add_pairing("proscuitto")
	all_melon_types.append(cren)

	yw = MelonType('yw', "yellow watermelon", 2013, 'yellow', False, True)
	yw.add_pairing("ice cream")
	all_melon_types.append(yw)

	return all_melon_types


melon_list = make_melon_types()


def print_pairing_info(melon_types):
	"""Prints information about each melon type's pairings."""
	for melon in melon_types:
		print("{} pairs with".format(melon.name.title()))
		for pairing in melon.pairings:
			print("- {}".format(pairing))


def make_melon_type_lookup(melon_types):
	"""Takes a list of MelonTypes and returns a dictionary of melon type by code."""
	melon_dictionary = {}
	for melon in melon_types:
		melon_dictionary[melon.code] = melon
	return melon_dictionary


############
# Part 2   #
############

class Melon(object):
	"""A melon in a melon harvest."""
	def __init__ (self, melon_code, shape_rating, color_rating, field_number, harvester):
		self.melon_code = melon_code
		self.shape_rating = shape_rating
		self.color_rating = color_rating
		self.field_number = field_number
		self.harvester = harvester.title()

	def is_sellable(self):
		""" Sets attribute to True/False depending on conditons"""
		if self.shape_rating >= 5 and self.color_rating >= 5 and self.field_number != 3:
			self.is_sellable = True
			return True
		else:
			self.is_sellable = False
			return False


def make_melons():
	"""Returns a list of Melon objects."""
	harvested_melons = []
	melon_harvested = Melon("yw", 8, 7, 2, "Sheila")
	harvested_melons.append(melon_harvested)
	melon_harvested = Melon("yw", 3, 4, 2, "Sheila")
	harvested_melons.append(melon_harvested)
	melon_harvested = Melon("yw", 9, 8, 3, "Sheila")
	harvested_melons.append(melon_harvested)
	melon_harvested = Melon("cas", 10, 6, 35, "Sheila")
	harvested_melons.append(melon_harvested)
	melon_harvested = Melon("cren", 8, 9, 35, "Michael")
	harvested_melons.append(melon_harvested)
	melon_harvested = Melon("cren", 8, 2, 35, "Michael")
	harvested_melons.append(melon_harvested)
	melon_harvested = Melon("cren", 2, 3, 4, "Michael")
	harvested_melons.append(melon_harvested)
	melon_harvested = Melon("musk", 6, 7, 4, "Michael")
	harvested_melons.append(melon_harvested)
	melon_harvested = Melon("yw", 7, 10, 3, "Sheila")
	harvested_melons.append(melon_harvested)

	return harvested_melons


def get_sellability_report(melons):
	"""Given a list of melon object, prints whether each one is sellable."""
	for melon in melons:
		melon.is_sellable()
		if melon.is_sellable is True:
			print("Harvested by {} from Field {} (CAN BE SOLD)".format(melon.harvester, melon.field_number))
		if melon.is_sellable is False:
			print("Harvested by {} from Field {} (NOT SELLABLE)".format(melon.harvester, melon.field_number))


harvest_melon_list = make_melons()
get_sellability_report(harvest_melon_list)


###################
# Further Study   #
###################

def update_harvest_melon_list(melon_list):
	""" Opens file, creates melon & attributes to update harvest_melon_list. """
	harvest_log = open("harvest_log.txt","r")
	for line in harvest_log:
		split_lines = line.split()
		melon_harvested = Melon(split_lines[5], int(split_lines[1]), int(split_lines[3]),
		 int(split_lines[11]), split_lines[8])
		melon_list.append(melon_harvested)
	return melon_list

harvest_melon_list = update_harvest_melon_list(harvest_melon_list)
