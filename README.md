# markov-weather-model
Markov chain weather forecasting model using Python
Modelling Workflow
1. Problem Definition/Motivation
I wanted to do weather forecasting with a Markov model because it's an interesting method of learning how weather patterns evolve over time. Weather forecasting is useful in a lot of aspects of our lives - from organizing outdoor activities to assisting farmers in deciding on their crops.
I reduced the weather to only three states in my model: Sunny (S), Cloudy (C), and Rainy (R). Although actual weather is more sophisticated, even such a simplified model can reveal some interesting patterns.
The central concept behind a Markov model is that the next state depends solely on the current state, not on the past history of how we arrived there. For weather, this would imply tomorrow's weather relies primarily on today's weather, rather than last week.
I like this model because:
It's straightforward enough to get but still demonstrates complicated behavior.
It encapsulates the unpredictability of weather.
It can help us perceive patterns in apparent random changes.

2. Model Formulation (Equations/Rules)
To perform this weather prediction activity, I  employed a first-order discrete-time Markov chain model. This was the most appropriate mathematical model to describe those random processes where the future state depends only on the present state and not on the past sequence of events leading to it. My weather model employs a transition matrix whose entries reflect the probability of transitioning from one weather state to another. I constructed this matrix as:



From/To
Sunny(S)
Cloudy(C)
Rainy(R)
Sunny 
0.6
0.3
0.1
Cloudy
0.4
0.3
0.3
Rainy
0.2
0.1
0.7



This implies that:
If today is Sunny, tomorrow will be Sunny with a 60% probability, Cloudy with a 30% chance, or Rainy with a 10% probability.
If today is Cloudy, tomorrow has a 40% chance of being Sunny, 30% chance of being Cloudy, and 30% chance of being Rainy.
If it's Rainy today, there's a 20% possibility that tomorrow will be Sunny, a 10% possibility that tomorrow will be Cloudy, and a 70% possibility that tomorrow will be Rainy.
3. Implementation of the Model 
To apply my weather model, I created a Python script that:
Declares the three states of weather: Sunny (S), Cloudy (C), and Rainy ®
Initializes my transition matrix to display the probabilities of transitioning from one state to another.
Begin with an initial state (I used Sunny).
Simulates the weather for 1000 days
Maintains a record of the order of weather states and the number of days spent in each state
The central part of my program is the random.choices() function, which allows me to choose the next state randomly based on the probabilities for the current state. For every day of my simulation, I:
Log the current state in my counts
Query the probabilities for transitions from the current state
Randomly choose the next state based on these probabilities
Set my current state to the newly chosen state
After executing all 1000 days, I print out the weather sequence and compute what proportion of days were in each state.

4. Exploration of the Model
4.1 Different Starting States
I was curious to see if my starting state would affect the long-term results, so I ran my simulation multiple times with different starting states (Sunny, Cloudy, and Rainy). I found that after 1000 days, the results were very close regardless of where I started:
When starting with Sunny:
Sunny days: 38.7% (387 days)
Cloudy days: 22.4% (224 days)
Rainy days: 38.9% (389 days)
When starting with Cloudy:
Sunny days: 39.1% (391 days)
Cloudy days: 21.9% (219 days)
Rainy days: 39.0% (390 days)
When starting with Rainy:
Sunny days: 38.5% (385 days)
Cloudy days: 22.3% (223 days)
Rainy days: 39.2% (392 days)
4.2 Varying Time Horizons
I was also interested in how the length of my simulation affects the results. I ran simulations for different numbers of days:
100 days:
Sunny: 42% (42 days)
Cloudy: 17% (17 days)
Rainy: 41% (41 days)
1000 days:
Sunny: 38.7% (387 days)
Cloudy: 22.4% (224 days)
Rainy: 38.9% (389 days)
5000 days:
Sunny: 39.1% (1955 days)
Cloudy: 21.9% (1095 days)
Rainy: 39.0% (1950 days)
I notice that the longer I run my simulation, the more stable the percentages become.


 
5. Conclusions
From my exploration of the Markov weather model, I learned several interesting things:
Effectiveness in Solving the Problem
My Markov model successfully represents elementary weather transition patterns and successfully produces realistic weather sequences that are consistent with our intuitive sense of weather persistence. For example, the model accurately indicates that rainy weather will last longer than cloudy weather. The model succeeds in its basic mission of illustrating how simple probabilistic rules can produce complex-looking weather patterns.
Personal Insights
Using this model has enriched my knowledge of stochastic processes. I've discovered that apparently random things like weather often can be described using surprisingly straightforward mathematical structures. The beauty of the Markov property - that we can make sensible predictions without a lot of historical data - is both beautiful and useful.
Limitations
This model has a number of significant limitations:
Seasonal invariance: The model is assuming weather acts the same throughout the year, which is not at all realistic. In the real world, transition probabilities would change enormously between summer and winter.
Geographical simplicity: The model is assuming weather is uniform by location, while actual weather systems differ enormously by geography.
Limited memory: By employing only a first-order Markov chain, we're assuming weather patterns don't have longer-term dependencies, which meteorologists know is not true.
Simplified states: Having only three weather states is a significant simplification that fails to represent temperature, humidity, wind, or precipitation intensity.
Static probabilities: The transition probabilities are static instead of changing to accommodate emerging patterns or external influences.

Simple vs. Complex Models
Although this model is simplistic, it does pose a significant question regarding model complexity. Are we absolutely required to have more complex models? For some uses (such as rough planning or gaining an understanding of simple weather patterns), this basic model may prove adequate. It is interpretable and computationally efficient.
But for real weather prediction, more sophisticated models are certainly required. The compromise is obvious: our simple model is easy to comprehend but restricted in accuracy, whereas sophisticated models are more accurate but less easy to interpret and computationally demanding.

According to me, this model could be improved/advanced by:
adding seasonal variations by using different transition matrices for different times of the year.
including more weather states for a more detailed model.
trying higher-order Markov models that look at multiple previous days.
including real historical weather data would result in more accurate transition probabilities.
Overall, I found this exploration of the Markov weather model very intriguing. Even with a simple three-state model, I was able to figure out interesting patterns and dynamics that help explain why weather forecasting is challenging yet fascinating.

