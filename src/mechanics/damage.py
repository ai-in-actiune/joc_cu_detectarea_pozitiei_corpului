class Fighter:
    def __init__(self, life=100, max_power=40):
        self.life = life
        self.maxLPA = 0.10 * self.life
        self.maxHPA = 0.18 * self.life
        self.shieldLPA = 0.05 * self.maxHPA
        self.shieldHPA = 0.20 * self.maxHPA
        self.power = 0
        self.maxPower = max_power

    def low_power_attack(self):
        damage = -0.10 * self.life
        power_increase = 0.10 * self.maxPower
        self.life += damage
        self.power += power_increase
        return damage

    def high_power_attack(self):
        damage = -0.18 * self.life
        power_decrease = -0.22 * self.maxPower
        self.life += damage
        self.power += power_decrease
        return damage

    def apply_shield(self, is_low_power_attack):
        if is_low_power_attack:
            damage_increase = 0.05 * self.maxLPA
            power_increase = 0.07 * self.maxLPA
        else:
            damage_increase = 0.20 * self.maxHPA
            power_increase = 0
        self.maxLPA += damage_increase
        self.power += power_increase

    def increase_max_power(self, is_low_power_attack, hpa_fraction=0.1, lpa_fraction=0.15):
        if is_low_power_attack:
            self.maxLPA += lpa_fraction * self.life
        else:
            self.maxHPA += hpa_fraction * self.life

        # Verify if power exceeds the maximum
        if self.power > self.maxPower:
            self.power = self.maxPower

    def print_status(self):
        print(f"Life: {self.life} points")
        print(f"Max LPA: {self.maxLPA} points")
        print(f"Max HPA: {self.maxHPA} points")
        print(f"Shield LPA: {self.shieldLPA} points")
        print(f"Shield HPA: {self.shieldHPA} points")
        print(f"Power: {self.power} points")
        print(f"Max Power: {self.maxPower} points")


# Example usage:
fighter = Fighter()
fighter.print_status()
print("Low Power Attack Damage:", fighter.low_power_attack())
fighter.apply_shield(True)
fighter.increase_max_power(True)
fighter.print_status()
print("High Power Attack Damage:", fighter.high_power_attack())
fighter.apply_shield(False)
fighter.increase_max_power(False)
fighter.print_status()