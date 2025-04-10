class Superhero:
    def __init__(self, name, secret_identity, powers, weakness, origin_story):
        self.name = name
        self.secret_identity = secret_identity
        self.powers = powers  # This should be a list
        self.weakness = weakness
        self.origin_story = origin_story
        self.energy_level = 100
        self.is_in_costume = False
    
    def put_on_costume(self):
        if not self.is_in_costume:
            self.is_in_costume = True
            return f"{self.secret_identity} transforms into {self.name}!"
        return f"{self.name} is already in costume."
    
    def use_power(self, power_index):
        if self.energy_level <= 0:
            return f"{self.name} is too exhausted to use powers!"
        
        if power_index < len(self.powers):
            power = self.powers[power_index]
            self.energy_level -= 10
            return f"{self.name} uses {power}! Energy level now at {self.energy_level}%"
        return "Power not found!"
    
    def rest(self):
        self.energy_level = min(100, self.energy_level + 30)
        return f"{self.name} rests. Energy level now at {self.energy_level}%"
    
    def encounter_weakness(self):
        self.energy_level = max(0, self.energy_level - 50)
        return f"Oh no! {self.name} encounters {self.weakness}! Energy drops to {self.energy_level}%"
    
    def __str__(self):
        return (f"Superhero: {self.name}\n"
                f"Secret Identity: {self.secret_identity}\n"
                f"Powers: {', '.join(self.powers)}\n"
                f"Weakness: {self.weakness}\n"
                f"Current Energy: {self.energy_level}%")

# Inheritance example - A specific type of superhero
class Mutant(Superhero):
    def __init__(self, name, secret_identity, powers, weakness, origin_story, mutation_level):
        super().__init__(name, secret_identity, powers, weakness, origin_story)
        self.mutation_level = mutation_level  # Scale from 1-10
    
    def mutate_further(self):
        if self.mutation_level < 10:
            self.mutation_level += 1
            new_power = f"Mutation Level {self.mutation_level} Power"
            self.powers.append(new_power)
            return f"{self.name} mutates further! Gained {new_power}"
        return f"{self.name} has reached maximum mutation level!"
    
    def use_power(self, power_index):
        # Mutants use powers more efficiently (only 5 energy cost)
        if self.energy_level <= 0:
            return f"{self.name} is too exhausted to use powers!"
        
        if power_index < len(self.powers):
            power = self.powers[power_index]
            self.energy_level -= 5  # Less energy cost than regular superhero
            return f"{self.name} uses {power} (mutant efficiency)! Energy level now at {self.energy_level}%"
        return "Power not found!"

# Example usage
if __name__ == "__main__":
    spider_man = Superhero(
        name="Spider-Man",
        secret_identity="Peter Parker",
        powers=["Web slinging", "Spider sense", "Wall crawling"],
        weakness="Ethyl chloride (bug spray)",
        origin_story="Bitten by a radioactive spider"
    )
    
    print(spider_man.put_on_costume())
    print(spider_man.use_power(0))
    print(spider_man.encounter_weakness())
    print(spider_man.rest())
    print()
    
    wolverine = Mutant(
        name="Wolverine",
        secret_identity="Logan",
        powers=["Healing factor", "Adamantium claws", "Enhanced senses"],
        weakness="Magnets",
        origin_story="Weapon X experiment",
        mutation_level=8
    )
    
    print(wolverine.put_on_costume())
    print(wolverine.use_power(1))  # Notice the different energy cost
    print(wolverine.mutate_further())
    print(wolverine)