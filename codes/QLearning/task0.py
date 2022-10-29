#!/usr/bin/env python
# coding=utf-8
'''
Author: John
Email: johnjim0816@gmail.com
Date: 2020-09-11 23:03:00
LastEditor: John
LastEditTime: 2022-10-30 01:37:24
Discription: 
Environment: 
'''
import sys,os
os.environ["KMP_DUPLICATE_LIB_OK"]  =  "TRUE" # avoid "OMP: Error #15: Initializing libiomp5md.dll, but found libiomp5md.dll already initialized."
curr_path = os.path.dirname(os.path.abspath(__file__))  # current path
parent_path = os.path.dirname(curr_path)  # parent path 
sys.path.append(parent_path)  # add path to system path

import gym
import datetime
import argparse
from envs.gridworld_env import FrozenLakeWapper
from envs.wrappers import CliffWalkingWapper
from envs.register import register_env
from qlearning import QLearning
from common.utils import all_seed,merge_class_attrs
from common.launcher import Launcher
from config.config import GeneralConfigQLearning,AlgoConfigQLearning

class Main(Launcher):
    def __init__(self) -> None:
        super().__init__()
        self.cfgs['general_cfg'] = merge_class_attrs(self.cfgs['general_cfg'],GeneralConfigQLearning())
        self.cfgs['algo_cfg'] = merge_class_attrs(self.cfgs['algo_cfg'],AlgoConfigQLearning())
    def env_agent_config(self,cfg,logger):
        ''' create env and agent
        '''  
        register_env(cfg.env_name)
        env = gym.make(cfg.env_name,new_step_api=False)  # create env
        if cfg.env_name == 'CliffWalking-v0':
            env = CliffWalkingWapper(env)
        if cfg.seed !=0: # set random seed
            all_seed(env,seed=cfg.seed) 
        try: # state dimension
            n_states = env.observation_space.n # print(hasattr(env.observation_space, 'n'))
        except AttributeError:
            n_states = env.observation_space.shape[0] # print(hasattr(env.observation_space, 'shape'))
        n_actions = env.action_space.n  # action dimension
        logger.info(f"n_states: {n_states}, n_actions: {n_actions}") # print info
        # update to cfg paramters
        setattr(cfg, 'n_states', n_states)
        setattr(cfg, 'n_actions', n_actions)
        agent = QLearning(cfg)
        return env,agent
    def train(self,cfg,env,agent,logger):
        logger.info("Start training!")
        logger.info(f"Env: {cfg.env_name}, Algorithm: {cfg.algo_name}, Device: {cfg.device}")
        rewards = []  # record rewards for all episodes
        steps = [] # record steps for all episodes
        for i_ep in range(cfg.train_eps):
            ep_reward = 0  # reward per episode
            ep_step = 0 # step per episode
            state = env.reset()  # reset and obtain initial state
            for _ in range(cfg.max_steps):
                action = agent.sample_action(state)  # sample action
                next_state, reward, terminated, _ = env.step(action)  # update env and return transitions
                agent.update(state, action, reward, next_state, terminated)  # update agent
                state = next_state  # update state
                ep_reward += reward
                ep_step += 1
                if terminated:
                    break
            rewards.append(ep_reward)
            steps.append(ep_step)
            logger.info(f'Episode: {i_ep+1}/{cfg.train_eps}, Reward: {ep_reward:.2f}: Epislon: {agent.epsilon:.3f}')
        logger.info("Finish training!")
        return {'episodes':range(len(rewards)),'rewards':rewards,'steps':steps}
    def test(self,cfg,env,agent,logger):
        logger.info("Start testing!")
        logger.info(f"Env: {cfg.env_name}, Algorithm: {cfg.algo_name}, Device: {cfg.device}")
        rewards = []  # record rewards for all episodes
        steps = [] # record steps for all episodes
        for i_ep in range(cfg.test_eps):
            ep_reward = 0  # reward per episode
            ep_step = 0
            state = env.reset()  # reset and obtain initial state
            for _ in range(cfg.max_steps):
                action = agent.predict_action(state)  # predict action
                next_state, reward, terminated, _ = env.step(action)  
                state = next_state 
                ep_reward += reward
                ep_step += 1
                if terminated:
                    break
            rewards.append(ep_reward)
            steps.append(ep_step)
            logger.info(f"Episode: {i_ep+1}/{cfg.test_eps}, Steps:{ep_step:d} Reward: {ep_reward:.2f}")
        logger.info("Finish testing!")
        return {'episodes':range(len(rewards)),'rewards':rewards,'steps':steps}

if __name__ == "__main__":
    main = Main()
    main.run()
   

        
    
