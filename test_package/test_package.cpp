#include <iostream>
#include <lua.hpp>

int main() {
    std::cout << LUA_RELEASE << std::endl;
    lua_State* L = luaL_newstate();
    luaL_openlibs(L);
    if (luaL_loadstring(L, "print(_VERSION)") != 0)
    {
        std::cerr << "error: " << lua_tostring(L, -1) << std::endl;
        return 1;
    }
    if (lua_pcall(L, 0, 0, 0) != 0)
    {
        std::cerr << "error: " << lua_tostring(L, -1) << std::endl;
        return 1;
    }
    lua_close(L);
}
