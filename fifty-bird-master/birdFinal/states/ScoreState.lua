--[[
    ScoreState Class
    Author: Colton Ogden
    cogden@cs50.harvard.edu

    A simple state used to display the player's score before they
    transition back into the play state. Transitioned to from the
    PlayState when they collide with a Pipe.
]]

ScoreState = Class{__includes = BaseState}

--[[
    When we enter the score state, we expect to receive the score
    from the play state so we know what to render to the State.
]]
local MEDAL_IMAGE = nil

function ScoreState:enter(params)
    self.score = params.score
    if self.score >= 25 then
        MEDAL_IMAGE = love.graphics.newImage('medal_1.png')
    elseif self.score >= 18 then
        MEDAL_IMAGE = love.graphics.newImage('medal_2.png')
    elseif self.score >= 10 then
        MEDAL_IMAGE = love.graphics.newImage('medal_3.png')
    else
        MEDAL_IMAGE = nil
    end
end

function ScoreState:update(dt)
    -- go back to play if enter is pressed
    if love.keyboard.wasPressed('enter') or love.keyboard.wasPressed('return') then
        gStateMachine:change('countdown')
    end
end

function ScoreState:render()
    -- simply render the score to the middle of the screen
    love.graphics.setFont(flappyFont)
    love.graphics.printf('Oof! You lost!', 0, 64, VIRTUAL_WIDTH, 'center')
    if MEDAL_IMAGE then
        love.graphics.draw(MEDAL_IMAGE, 10,5)
    end
    love.graphics.setFont(mediumFont)
    love.graphics.printf('Score: ' .. tostring(self.score), 0, 100, VIRTUAL_WIDTH, 'center')

    love.graphics.printf('Press Enter to Play Again!', 0, 160, VIRTUAL_WIDTH, 'center')
end