#创建环境
import gym
from gym import spaces
import numpy as np

class kpr_stock(gym.Env):
    
    metadata = {'render.modes': ['human', 'ansi']}


    def __init__(self):
        super(kpr_stock, self).__init__()
        self.action_space = spaces.Discrete(3) # 0, 1, 2: 買入，賣出，觀望
        self.observation_space = spaces.Box(np.array([0, 0]), np.array([10000000, 10]))
        self.state = None
        self.init_money = 10000
        self.cur_money = self.init_money
        self.cur_stock_money = 0
        self.t = 0
        self.stock_data = self.load_stock_data()
        self.pre_all_money = self.init_money
        self.hold_stock_num = 0
        
    def step(self, action):
        assert self.action_space.contains(action), "%r (%s) invalid"%(action, type(action))
        
        if (self.t + 1 >= len(self.stock_data)) or (self.cur_money <= 0):
            done = True
            reward = 0
            return self.state, reward, done, {}

        #買入
        if action == 0 and self.cur_money >= 100 * self.stock_data[self.t]:
            self.cur_money -= 100 * self.stock_data[self.t]
            self.cur_stock_money += 100 * self.stock_data[self.t]
            self.hold_stock_num += 100
            
        #賣出
        if action == 1 and self.hold_stock_num > 0:
            self.cur_money += self.hold_stock_num * self.stock_data[self.t]
            self.cur_stock_money = 0
            self.hold_stock_num = 0
        
        #觀望
        if action == 2:
            pass
                    
                   
        self.t += 1
        profit = self.cur_money + self.cur_stock_money - self.pre_all_money
        
        reward = profit

        self.pre_all_money = self.cur_money + self.cur_stock_money
        self.state = np.array([self.pre_all_money, self.stock_data[self.t]])
        done = False
        
        return self.state, reward, done, {}


    def reset(self):
        self.state = np.array([self.init_money, 0])
        self.cur_money = self.init_money
        self.cur_stock_money = 0
        self.t = 0
        self.pre_all_money = self.init_money
        self.hold_stock_num = 0
        return self.state


    def load_stock_data(self):
        return np.array([9,1,9,1,9,1])
    
    
    def render(self, mode='human'):
        return None


    def close(self):
        return None


#测试环境

gym.logger.set_level(40)
env = kpr_stock()
for i_episode in range(1000):
    observation = env.reset()
    reward_sum = 0
    save_step = []
    for t in range(10):
        #print(observation)
        action = env.action_space.sample()
        observation, reward, done, info = env.step(action)
        reward_sum += reward
        save_step.append(action)
        #print(action, observation[0])
        if done:
            print(observation[0], reward_sum)
            break

env.close()
