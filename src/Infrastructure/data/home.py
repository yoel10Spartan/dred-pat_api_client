from Infrastructure.data.settings import DataBaseSQL
from Resources.config.environment import get_settings
from Infrastructure.data.models import archeology
from Infrastructure.data.models import t12_unidades_u_x_y
from Infrastructure.data.models import t27_unidad_z

_SETTINGS = get_settings()

# ========================================================================================

data_base_globlal_sistem = DataBaseSQL(_SETTINGS.DATABASE_PG_URL, archeology.Base)
OpenConection = data_base_globlal_sistem.start()

# # ========================================================================================

data_base_t12 = DataBaseSQL(_SETTINGS.DATABASE_PG_URL_T12, t12_unidades_u_x_y.Base)
OpenConectionT12 = data_base_t12.start()

# # ========================================================================================

data_base_t27 = DataBaseSQL(_SETTINGS.DATABASE_PG_URL_T27, t27_unidad_z.Base)
OpenConectionT27 = data_base_t27.start()