<script>
  let weight = 70; // Körpergewicht in kg, Standardwert
  let gender = "male"; // "male" oder "female"
  let hours = 0; // Zeit seit Konsum in Stunden
  let minutes = 0; // Zeit seit Konsum in Minuten
  let result = null; // Ergebnis des Promillewerts
  let soberTime = null; // Zeit, bis Fahrtauglichkeit erreicht ist
  let isFitToDrive = null; // Fahrtauglichkeit

const drinks = [
    { name: "Bier", volume: 500, alcoholPercent: 5, count: 0, emoji: "🍺" },
    { name: "Cocktail", volume: 200, alcoholPercent: 12, count: 0, emoji: "🍸" },
    { name: "Rotwein", volume: 200, alcoholPercent: 12, count: 0, emoji: "🍷" },
    { name: "Kurze", volume: 20, alcoholPercent: 40, count: 0, emoji: "🥃" }
  ];

const calculateBAC = () => {
    const reductionFactor = gender === "male" ? 0.68 : 0.55;
    // Minuten in Stunden umrechnen und addieren
    const totalHours = hours + minutes / 60;
    // Gesamtalkoholmenge berechnen
    const totalAlcoholInGrams = drinks.reduce(
      (sum, drink) =>
        sum + drink.count * drink.volume * (drink.alcoholPercent / 100) * 0.8,
      0
    );
    // Promillewert berechnen
    const bac = totalAlcoholInGrams / (weight * reductionFactor) - 0.15 * totalHours;
    result = Math.max(0, bac).toFixed(2); // Keine negativen Werte

    // Fahrtauglichkeit
    isFitToDrive = bac <= 0.3;
    // Zeit bis Fahrtauglichkeit berechnen (unter 0.3‰)
    const soberHours = bac > 0 ? bac / 0.15 : 0; // Stunden bis 0.3 Promille
    soberTime = Math.max(0, soberHours - totalHours); // Abziehen der bereits vergangenen Zeit
    // Computergenerierte Stimme für verschiedene BAC-Bereiche
    speakBasedOnBAC(bac);
};


const incrementDrink = (index) => drinks[index].count++;

const decrementDrink = (index) => {
    if (drinks[index].count > 0) {
      drinks[index].count--; // Nur verringern, wenn mehr als 0
    }
  };

const incrementHours = () => hours++;
const decrementHours = () => {
    if (hours > 0) hours--;
  };

const incrementMinutes = () => {
    if (minutes < 59) minutes++;
  };
 
const decrementMinutes = () => {
    if (minutes > 0) minutes--;
  };

const formatSoberTime = (timeInHours) => {
    const hours = Math.floor(timeInHours);
    const minutes = Math.round((timeInHours - hours) * 60);
    return `${hours}h ${minutes}m`;
  };

const speakBasedOnBAC = (bac) => {
    const msg = new SpeechSynthesisUtterance();
    if (bac >= 3.5) {
      msg.text = "Tatütatatatütata.";
    } else if (bac >= 1.5) {
      msg.text = "So ein Tag, so wunderschön wie heute.";
    } else if (bac >= 0.91) {
      msg.text = "Huiuiuiuiuiuiuiui.";
    } else if (bac >= 0 && bac <= 0.9) {
      msg.text = "Einer geht noch, einer geht noch rein.";
    } else {
			msg.text = "Nicht lang schnacken, Kopf in Nacken."
		}
    window.speechSynthesis.speak(msg);
};
</script>

<style>
  .calculator {
    max-width: 400px;
    margin: 0 auto;
    padding: 1em;
    border: 1px solid #ddd;
    border-radius: 8px;
    font-family: Arial, sans-serif;
  }

.gender-selection {
    display: flex;
    justify-content: space-around;
    margin-bottom: 1em;
  }

.gender-button {
    width: 100px;
    height: 100px;
    border-radius: 50%;
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 2em;
    cursor: pointer;
    background-color: #f9f9f9;
    border: 2px solid #ddd;
    transition: background-color 0.3s;
  }

.gender-button.active {
    background-color: #007BFF;
    color: white;
}

.drink-selection {
    display: flex;
    margin-bottom: 1em;
	 display: flex;
  justify-content: center;
  align-items: center;
}

.drink-button {
    text-align: center;
    cursor: pointer;
		font-family: "Verdana";
    font-size: 1em;
  }
	
 .result {
    margin-top: 1em;
    padding: 1em;
    border-radius: 8px;
    text-align: center;
    font-size: 1.2em;
    font-weight: bold;
  }

.result.unfit {
    color: red;
  }

.result.fit {
    color: green;
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 0.5em;
  }

.sober-time {
    margin-top: 1em;
    padding: 1em;
    background-color: #f1f8e9;
    border: 1px solid #cddc39;
    border-radius: 8px;
    text-align: center;
    font-size: 1em;
    color: #558b2f;
    font-weight: bold;
}

.alert {
    color: red;
    font-size: 1.2em;
    font-weight: bold;
    margin-top: 1em;
    text-align: center;
  }

input, select {
    width: 100%;
    padding: 0.5em;
    margin: 0.5em 0;
    border: 1px solid #ccc;
    border-radius: 4px;
  }

button.calculate {
    width: 100%;
    padding: 0.7em;
    background-color: #007BFF;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 1.2em;
  }

button.calculate:hover {
    background-color: #0056b3;
  }

  /* Stil für die Plus- und Minus-Buttons */

small {
	font-family:Verdana;
	font-size:9px;
	line-height:1px;
	margin: 0;
  padding: 0;
	display:inline;
}
	
button {
    width: 32px;
    height: 32px;
    font-size: 1em;
    background-color: #007BFF;
    color: white;
    border: none;
    border-radius: 50%;
    margin: 0.2em;
    cursor: pointer;
  }

button:hover {
    background-color: #0056b3;
  }

  /* Stil für den Minus-Button (minimalistisch) */

button.decrement {
    background-color: #e74c3c; /* Rot */
    color: white;
    font-size: 1em;
  }

button.decrement:hover {
    background-color: #c0392b; /* Dunkleres Rot */
  }
	
button.decrement:focus {
    outline: none;
  }

  /* Buttons für Zeit */
  .time-buttons {
    display: flex;
    justify-content: space-between;
    width: 100%;
    margin-bottom: 1em;
  }

  .time-button {
    width: 50px;
    height: 50px;
    font-size: 1.5em;
    background-color: #f1f1f1;
    color: #333;
    border: 1px solid #ddd;
    border-radius: 50%;
    display: flex;
    justify-content: center;
    align-items: center;
    cursor: pointer;
  }
 
  .time-button:hover {
    background-color: #e0e0e0;
  }
</style>

<div class="calculator">
  <h3>Berechnung des Blutalkoholwerts</h3>
  <!-- Eingabefeld für Körpergewicht -->
  <label for="weight">Körpergewicht (kg):</label>
  <input id="weight" type="number" bind:value={weight} min="1" max="500" />
 
  <!-- Eingabefeld für Zeit -->
  <label for="time">Zeit nach Konsum:</label>
  <div class="time-buttons">
    <button class="time-button" on:click={decrementHours}>-</button>
    <span>{hours}h</span>
    <button class="time-button" on:click={incrementHours}>+</button>
    <button class="time-button" on:click={decrementMinutes}>-</button>
    <span>{minutes}m</span>
    <button class="time-button" on:click={incrementMinutes}>+</button>
  </div>
 
  <div class="gender-selection">
    <div class="gender-button {gender === 'male' ? 'active' : ''}" on:click={() => gender = 'male'}>
      M
    </div>
    <div class="gender-button {gender === 'female' ? 'active' : ''}"
      on:click={() => gender = 'female'}>
      W
    </div>
  </div>
  <div class="drink-selection">
    {#each drinks as drink, index}
      <div class="drink-button">
        <div on:click={() => incrementDrink(index)}>
          {drink.emoji} {drink.name} ({drink.count})
        </div>
        <div>
          <button class="decrement" on:click={() => decrementDrink(index)}>-</button>
        </div>
      </div>
    {/each}
  </div>
  <button class="calculate" on:click={calculateBAC}>Berechnen</button>
  {#if result !== null}
    <div class="result {isFitToDrive ? 'fit' : 'unfit'}">
      {isFitToDrive ? "Du kannst fahren!" : "Du bist nicht fahrtauglich!"}
    </div>
    <div class="sober-time">
      Bis zur Fahrtauglichkeit: {formatSoberTime(soberTime)}
    </div>
    <div class="result">
      Blutalkoholwert: {result} ‰
    </div>
  {/if}

  {#if result !== null && result > 0.3}
    <div class="alert">Warnung: Du bist weit über dem gesetzlichen Grenzwert!</div>
  {/if}
</div>
<hr>
<div><small>Code von Benjamin Hofmann und Esther Stosch im Rahmen des Seminars <a href="https://abp.de/seminar/Programmieren_f%C3%BCr_Journalisten/541/" target="_blank">"Programmieren für Journos" der Akademie der Bayerischen Presse</a></small></div>