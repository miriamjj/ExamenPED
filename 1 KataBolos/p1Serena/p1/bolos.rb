class Partida
    
    def numero_rondas_correcto(rondas)
        return rondas.length == 10 || (rondas.length == 11 && (comprobar_strike(rondas[9]) == 1 || comprobar_spare(rondas[9])))
    end

    def bolas_ronda_correctas(rondas)
        for ronda in rondas
            if ronda.length == 2 && ronda[0] >= 0 && ronda[1] >= 0 && ronda[0] + ronda[1] <= 10
                return true
            elsif ronda.length == 1 && ronda[0] >= 0 
                return true
            else
                return false
            end
        end
    end

    def strike(num_strike, ronda, num_ronda)
        @puntos = 0
        if num_strike == 1
            @puntos = @puntos + 10 + 2*(ronda[0] + ronda[1])
        elsif num_strike > 1
            @puntos = @puntos + (num_strike - 1)*3*10 + 3*ronda[0] + 2*ronda[1]
        end
        if num_ronda == 11
            @puntos = @puntos - ronda[0] - ronda[1]
        end
        return @puntos
    end

    def spare(ronda, num_ronda)
        @puntos = 0
        if comprobar_strike(ronda) == 1 || num_ronda == 11
            @puntos = @puntos + ronda[0] 
        else
            @puntos = @puntos + 2*ronda[0] + ronda[1]
        end
        return @puntos
    end

    def comprobar_spare(ronda)
        if ronda.length == 2
            return ronda[0] + ronda[1] == 10
        end
    end

    def comprobar_strike(ronda)
        if ronda.length == 1 && ronda[0] == 10
            return 1
        else
            return 0
        end
    end

    def puntuacion_partida(rondas)
        @puntuacion = 0
        @strike = 0
        @spare = false
        @num_ronda = 0
        if numero_rondas_correcto(rondas) && bolas_ronda_correctas(rondas)
            for ronda in rondas
                @num_ronda += 1
                if @strike > 0 && ronda.length == 2
                    @puntuacion = @puntuacion + strike(@strike, ronda, @num_ronda)
                    @strike = 0
                elsif @spare
                    @puntuacion = @puntuacion + spare(ronda, @num_ronda) 
                elsif ronda.length == 2
                    @puntuacion = @puntuacion + ronda[0] + ronda[1]
                end 
                @strike = @strike + comprobar_strike(ronda)
                @spare = comprobar_spare(ronda)
            end
            return @puntuacion

        end
    end

end