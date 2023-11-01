import gymnasium as gym

gym.register(id="Gecko", entry_point="envs.gecko:Gecko")

env = gym.make("Gecko", render_mode="human")
observation, info = env.reset(seed=42)

for _ in range(1000):
    action = env.action_space.sample()
    observation, reward, terminated, truncated, info = env.step(action)

    if terminated or truncated:
        observation, info = env.reset()

    env.render()

env.close()
