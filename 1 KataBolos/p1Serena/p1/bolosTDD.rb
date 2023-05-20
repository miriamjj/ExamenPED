require "test/unit"
require_relative 'bolos'

class BolosTDD < Test::Unit::TestCase

    def test_comprobar_rondas
        partida = Partida.new
        rondas = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
        assert_true(partida.numero_rondas_correcto(rondas))
    end

    def test_comprobar_rondas_excede_10
        partida = Partida.new
        rondas = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
        assert_false(partida.numero_rondas_correcto(rondas))
    end

    def test_comprobar_rondas_menor_10
        partida = Partida.new
        rondas = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
        assert_false(partida.numero_rondas_correcto(rondas))
    end

    def test_comprobar_puntos_0
        partida = Partida.new()
        rondas = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
        assert_equal(0, partida.puntuacion_partida(rondas))
    end

    def test_comprobar_puntos_6
        partida = Partida.new()
        rondas = [[3, 1], [2, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
        assert_equal(6, partida.puntuacion_partida(rondas))
    end

    def test_comprobar_puntos_23
        partida = Partida.new()
        rondas = [[3, 6], [2, 0], [3, 4], [0, 0], [0, 5], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
        assert_equal(23, partida.puntuacion_partida(rondas))
    end

    def test_comprobar_puntos_43
        partida = Partida.new()
        rondas = [[3, 6], [2, 0], [3, 4], [0, 3], [0, 5], [0, 0], [4, 4], [0, 0], [9, 0], [0, 0]]
        assert_equal(43, partida.puntuacion_partida(rondas))
    end

    def test_strike
        partida = Partida.new()
        rondas = [[10, ], [1, 2], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
        assert_equal(16, partida.puntuacion_partida(rondas))
    end

    def test_strike_2
        partida = Partida.new()
        rondas = [[10, ], [2, 4], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
        assert_equal(22, partida.puntuacion_partida(rondas))
    end

    def test_strike_en_medio
        partida = Partida.new()
        rondas = [[1, 0], [2, 4], [0, 0], [10, ], [3, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
        assert_equal(23, partida.puntuacion_partida(rondas))
    end

    def test_dos_strikes
        partida = Partida.new()
        rondas = [[10, ], [2, 4], [0, 0], [10, ], [3, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
        assert_equal(38, partida.puntuacion_partida(rondas))
    end

    def test_dos_strikes_seguidos
        partida = Partida.new()
        rondas = [[10, ], [10, ], [3, 4], [1, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
        assert_equal(48, partida.puntuacion_partida(rondas))
    end

    def test_dos_strikes_seguidos_2
        partida = Partida.new()
        rondas = [[10, ], [10, ], [3, 4], [10, ], [1, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
        assert_equal(59, partida.puntuacion_partida(rondas))
    end

    def test_tres_strikes_seguidos
        partida = Partida.new()
        rondas = [[10, ], [10, ], [10, ], [1, 2], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
        assert_equal(67, partida.puntuacion_partida(rondas))
    end

    def test_cuatro_strikes_seguidos
        partida = Partida.new()
        rondas = [[10, ], [10, ], [10, ], [10, ], [3, 5], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
        assert_equal(109, partida.puntuacion_partida(rondas))
    end

    def test_strikes_seguidos_medio
        partida = Partida.new()
        rondas = [[2, 4], [10, ], [10, ], [10, ], [3, 5], [10, ], [10, ], [1, 2], [0, 0], [0, 0]]
        assert_equal(122, partida.puntuacion_partida(rondas))
    end

    def test_spare
        partida = Partida.new()
        rondas = [[3, 7], [1, 2], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
        assert_equal(14, partida.puntuacion_partida(rondas))
    end

    def test_dos_spares
        partida = Partida.new()
        rondas = [[3, 7], [1, 2], [0, 0], [4, 6], [3, 2], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
        assert_equal(32, partida.puntuacion_partida(rondas))
    end

    def test_dos_spares_seguidos
        partida = Partida.new()
        rondas = [[3, 7], [8, 2], [4, 0], [4, 0], [3, 2], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
        assert_equal(45, partida.puntuacion_partida(rondas))
    end

    def test_tres_spares_seguidos
        partida = Partida.new()
        rondas = [[3, 7], [8, 2], [4, 6], [4, 0], [3, 2], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
        assert_equal(55, partida.puntuacion_partida(rondas))
    end

    def test_cuatro_spares_seguidos
        partida = Partida.new()
        rondas = [[3, 7], [8, 2], [4, 6], [4, 6], [3, 2], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
        assert_equal(64, partida.puntuacion_partida(rondas))
    end

    def test_spares_seguidos_medio
        partida = Partida.new()
        rondas = [[3, 7], [8, 2], [1, 6], [4, 6], [8, 2], [2, 1], [0, 0], [0, 0], [0, 0], [0, 0]]
        assert_equal(69, partida.puntuacion_partida(rondas))
    end

    def test_strike_luego_spare
        partida = Partida.new()
        rondas = [[10, ], [8, 2], [1, 6], [4, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
        assert_equal(42, partida.puntuacion_partida(rondas))
    end

    def test_spare_luego_strike
        partida = Partida.new()
        rondas = [[8, 2], [10, ], [1, 6], [4, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
        assert_equal(48, partida.puntuacion_partida(rondas))
    end

    def test_mezcla_spares_strikes
        partida = Partida.new()
        rondas = [[1, 2], [10, ], [1, 9], [4, 6], [10, ], [10, ], [1, 2], [0, 0], [0, 0], [0, 0]]
        assert_equal(94, partida.puntuacion_partida(rondas))
    end

    def test_strike_ultima_ronda
        partida = Partida.new()
        rondas = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [10, ], [3, 4]]
        assert_equal(17, partida.puntuacion_partida(rondas))
    end

    def test_dos_strike_ultimas_rondas
        partida = Partida.new()
        rondas = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [10, ], [10, ], [3, 4]]
        assert_equal(40, partida.puntuacion_partida(rondas))
    end

    def test_spare_ultima_ronda
        partida = Partida.new()
        rondas = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [6, 4], [3, ]]
        assert_equal(13, partida.puntuacion_partida(rondas))
    end

    def test_spare_dos_ultimas_rondas
        partida = Partida.new()
        rondas = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [1, 9], [6, 4], [3, ]]
        assert_equal(29, partida.puntuacion_partida(rondas))
    end

    def test_strike_spare_dos_ultimas_rondas
        partida = Partida.new()
        rondas = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [10, ], [6, 4], [3, ]]
        assert_equal(33, partida.puntuacion_partida(rondas))
    end

    def test_strike_spare_ultimas_rondas
        partida = Partida.new()
        rondas = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [10, ], [2, 8], [10, ], [3, 5]]
        assert_equal(58, partida.puntuacion_partida(rondas))
    end

    def test_ronda_3_bolas
        partida = Partida.new()
        rondas = [[0, 0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
        assert_false(partida.bolas_ronda_correctas(rondas))
    end

    def test_ronda_0_bolas
        partida = Partida.new()
        rondas = [[], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
        assert_false(partida.bolas_ronda_correctas(rondas))
    end

    def test_ronda_bolas_negativas
        partida = Partida.new()
        rondas = [[-1, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
        assert_false(partida.bolas_ronda_correctas(rondas))
    end

    def test_ronda_bolas_negativas_2
        partida = Partida.new()
        rondas = [[-1, -3], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
        assert_false(partida.bolas_ronda_correctas(rondas))
    end

    def test_ronda_mas_10_puntos
        partida = Partida.new()
        rondas = [[8, 4], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
        assert_false(partida.bolas_ronda_correctas(rondas))
    end

end
